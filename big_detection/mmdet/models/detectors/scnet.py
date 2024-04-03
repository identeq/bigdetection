# from ..builder import DETECTORS
# from .cascade_rcnn import CascadeRCNN
from big_detection.mmdet.models.builder import DETECTORS
from big_detection.mmdet.models.detectors.cascade_rcnn import CascadeRCNN


@DETECTORS.register_module()
class SCNet(CascadeRCNN):
    """Implementation of `SCNet <https://arxiv.org/abs/2012.10150>`_"""

    def __init__(self, **kwargs):
        super(SCNet, self).__init__(**kwargs)
