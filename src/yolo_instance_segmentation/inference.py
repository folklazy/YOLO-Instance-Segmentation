"""Portable extraction of the application's YOLO person prediction contract.

Source identity and exact settings are recorded in configs/selected_yolo26x.json.
Model loading is explicit and requires an existing hash-verified checkpoint.
"""
from pathlib import Path
import hashlib
import numpy as np

SELECTED_CHECKPOINT_SHA256 = '92b3de0065766a17180d6219858717dc9d03cdce8a3ca9576c97fd75aabb64f3'


def verify_checkpoint(path, expected_sha256):
    path = Path(path).resolve()
    if not path.is_file():
        raise FileNotFoundError(f'Provide the local checkpoint at {path}')
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    if digest.hexdigest() != expected_sha256:
        raise ValueError('YOLO_CHECKPOINT_HASH_MISMATCH')
    return path


class PersonSegmenter:
    """Predict independent native-grid person masks from one uint8 RGB image."""

    def __init__(self, checkpoint, device='cuda:0', expected_sha256=SELECTED_CHECKPOINT_SHA256):
        path = verify_checkpoint(checkpoint, expected_sha256)
        import torch
        from ultralytics import YOLO
        torch.set_num_threads(2)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        self.model = YOLO(str(path))
        if self.model.task != 'segment' or self.model.names.get(0) != 'person':
            raise ValueError('Person instance segmentation checkpoint required')
        self.device = device
        self.checkpoint_sha256 = expected_sha256

    def predict_rgb(self, rgb, confidence=0.25):
        if not isinstance(rgb, np.ndarray) or rgb.dtype != np.uint8 or rgb.ndim != 3:
            raise ValueError('Expected uint8 RGB HxWx3 image')
        if rgb.shape[2] != 3 or min(rgb.shape[:2]) <= 0:
            raise ValueError('Expected nonempty RGB image')
        if not np.isfinite(confidence) or not 0 <= confidence <= 1:
            raise ValueError('Confidence must be finite in [0,1]')
        import cv2
        import torch
        with torch.inference_mode():
            result = self.model.predict(
                cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), device=self.device,
                classes=[0], imgsz=640, conf=float(confidence), iou=0.7,
                max_det=200, retina_masks=True, half=False, augment=False,
                verbose=False, save=False,
            )[0]
        height, width = rgb.shape[:2]
        boxes = result.boxes.xyxy.cpu().numpy()
        scores = result.boxes.conf.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()
        if classes.shape != scores.shape or not np.all(classes == 0):
            raise ValueError('DETECTOR_PERSON_CLASS_CONTRACT')
        if len(boxes) and result.masks is None:
            raise ValueError('DETECTOR_MISSING_INSTANCE_MASK')
        masks = (result.masks.data.cpu().numpy() > 0.5
                 if len(boxes) else np.empty((0, height, width), bool))
        if (boxes.shape != (len(scores), 4) or masks.shape != (len(boxes), height, width)
                or not np.isfinite(boxes).all() or not np.isfinite(scores).all()):
            raise ValueError('DETECTOR_GEOMETRY_CONTRACT')
        if len(masks) and not np.all(np.any(masks.reshape(len(masks), -1), axis=1)):
            raise ValueError('DETECTOR_EMPTY_INSTANCE_MASK')
        return dict(boxes=boxes, scores=scores, masks=masks,
                    class_ids=classes.astype(np.int64), original_wh=[width, height])
