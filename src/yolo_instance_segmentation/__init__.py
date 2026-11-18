"""Selected YOLO inference interface and independently scoped research evaluators."""
from .inference import PersonSegmenter, SELECTED_CHECKPOINT_SHA256
__version__ = '0.1.0'
__all__ = ['PersonSegmenter', 'SELECTED_CHECKPOINT_SHA256']
