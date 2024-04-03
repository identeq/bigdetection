from big_detection.mmdet.datasets.builder import DATASETS
from big_detection.mmdet.datasets.coco import CocoDataset


@DATASETS.register_module()
class DeepFashionDataset(CocoDataset):

    CLASSES = ('top', 'skirt', 'leggings', 'dress', 'outer', 'pants', 'bag',
               'neckwear', 'headwear', 'eyeglass', 'belt', 'footwear', 'hair',
               'skin', 'face')
