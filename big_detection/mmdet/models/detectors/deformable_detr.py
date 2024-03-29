# from ..builder import DETECTORS
# from .detr import DETR
from big_detection.mmdet.models.builder import DETECTORS
from big_detection.mmdet.models.detectors.detr import DETR


@DETECTORS.register_module()
class DeformableDETR(DETR):

    def __init__(self, *args, **kwargs):
        super(DETR, self).__init__(*args, **kwargs)
