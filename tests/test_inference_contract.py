"""CPU contract checks against the application's exact detector arguments."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import json
import tempfile
import unittest
from unittest.mock import Mock, patch

import numpy as np
import torch
from yolo_instance_segmentation.inference import PersonSegmenter, verify_checkpoint

ROOT = Path(__file__).resolve().parents[1]


def result(boxes, scores, classes, masks):
    return SimpleNamespace(
        boxes=SimpleNamespace(xyxy=torch.tensor(boxes).reshape(-1, 4),
            conf=torch.tensor(scores), cls=torch.tensor(classes)),
        masks=SimpleNamespace(data=torch.tensor(masks)) if masks is not None else None)


class DetectorContract(unittest.TestCase):
    def setUp(self):
        self.segmenter = PersonSegmenter.__new__(PersonSegmenter)
        self.segmenter.device = 'cpu'
        self.segmenter.model = Mock()
        self.rgb = np.zeros((7, 11, 3), np.uint8)
        self.rgb[1, 8] = [17, 53, 201]

    def test_asymmetric_geometry_rgb_and_exact_application_settings(self):
        masks = np.zeros((2, 7, 11), np.float32)
        masks[0, 1:4, 2:5] = 1
        masks[1, 3:6, 7:10] = 1
        self.segmenter.model.predict.return_value = [result([[2,1,5,4],[7,3,10,6]], [.8,.9],[0,0],masks)]
        actual = self.segmenter.predict_rgb(self.rgb)
        passed, kwargs = self.segmenter.model.predict.call_args
        np.testing.assert_array_equal(passed[0][1,8], [201,53,17])
        np.testing.assert_array_equal(actual['masks'], masks.astype(bool))
        self.assertEqual(actual['original_wh'], [11,7])
        expected = json.loads((ROOT/'configs/selected_yolo26x.json').read_text())['predict_kwargs']
        self.assertEqual(kwargs, dict(expected, device='cpu'))

    def test_no_people_preserves_original_empty_mask_grid(self):
        self.segmenter.model.predict.return_value = [result([],[],[],None)]
        actual = self.segmenter.predict_rgb(self.rgb)
        self.assertEqual(actual['masks'].shape, (0,7,11))
        self.assertEqual(actual['boxes'].shape, (0,4))

    def test_wrong_native_grid_rejected(self):
        self.segmenter.model.predict.return_value = [result([[0,0,1,1]],[.8],[0],np.ones((1,11,7)))]
        with self.assertRaisesRegex(ValueError, 'GEOMETRY'):
            self.segmenter.predict_rgb(self.rgb)

    def test_detection_without_mask_rejected(self):
        self.segmenter.model.predict.return_value = [result([[0,0,1,1]],[.8],[0],None)]
        with self.assertRaisesRegex(ValueError, 'MISSING_INSTANCE_MASK'):
            self.segmenter.predict_rgb(self.rgb)

    def test_nonperson_and_nonfinite_outputs_rejected(self):
        for classes, boxes in [([1],[[0,0,1,1]]),([0],[[float('nan'),0,1,1]])]:
            self.segmenter.model.predict.return_value = [result(boxes,[.8],classes,np.ones((1,7,11)))]
            with self.assertRaises(ValueError):
                self.segmenter.predict_rgb(self.rgb)

    def test_empty_instance_mask_rejected(self):
        self.segmenter.model.predict.return_value = [result([[0,0,1,1]],[.8],[0],np.zeros((1,7,11)))]
        with self.assertRaisesRegex(ValueError,'EMPTY_INSTANCE_MASK'):
            self.segmenter.predict_rgb(self.rgb)

    def test_invalid_input_and_confidence_rejected_before_model(self):
        for image in [self.rgb.astype(np.float32), np.empty((0,11,3),np.uint8), self.rgb[:,:,0]]:
            with self.assertRaises(ValueError):
                self.segmenter.predict_rgb(image)
        for confidence in [float('nan'),-1,2]:
            with self.assertRaises(ValueError):
                self.segmenter.predict_rgb(self.rgb,confidence)
        self.segmenter.model.predict.assert_not_called()

    def test_checkpoint_missing_and_wrong_hash_stop_before_loading(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'model.pt'
            with self.assertRaises(FileNotFoundError):
                verify_checkpoint(path,'unused')
            path.write_bytes(b'literal test content')
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(verify_checkpoint(path,digest),path)
            with self.assertRaisesRegex(ValueError,'HASH_MISMATCH'):
                verify_checkpoint(path,'0'*64)


    def test_loading_preserves_application_precision_process_settings(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'model.pt'
            path.write_bytes(b'loading guard fixture')
            expected=hashlib.sha256(path.read_bytes()).hexdigest()
            with patch('ultralytics.YOLO') as factory:
                factory.return_value.task='segment'
                factory.return_value.names={0:'person'}
                detector=PersonSegmenter(path,device='cpu',expected_sha256=expected)
                factory.assert_called_once_with(str(path))
                detector.model.predict.assert_not_called()
                self.assertFalse(torch.backends.cuda.matmul.allow_tf32)
                self.assertFalse(torch.backends.cudnn.allow_tf32)
                self.assertEqual(torch.get_num_threads(),2)
