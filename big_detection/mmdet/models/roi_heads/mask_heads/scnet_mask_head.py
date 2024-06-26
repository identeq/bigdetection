# from big_detection.mmdet.models import HEADS
# from .fcn_mask_head import FCNMaskHead
# from ...utils import ResLayer, SimplifiedBasicBlock
from big_detection.mmdet.models.builder import HEADS
from big_detection.mmdet.models.roi_heads.mask_heads.fcn_mask_head import FCNMaskHead
from big_detection.mmdet.models.utils.res_layer import ResLayer, SimplifiedBasicBlock


@HEADS.register_module()
class SCNetMaskHead(FCNMaskHead):
    """Mask head for `SCNet <https://arxiv.org/abs/2012.10150>`_.

    Args:
        conv_to_res (bool, optional): if True, change the conv layers to
            ``SimplifiedBasicBlock``.
    """

    def __init__(self, conv_to_res=True, **kwargs):
        super(SCNetMaskHead, self).__init__(**kwargs)
        self.conv_to_res = conv_to_res
        if conv_to_res:
            assert self.conv_kernel_size == 3
            self.num_res_blocks = self.num_convs // 2
            self.convs = ResLayer(
                SimplifiedBasicBlock,
                self.in_channels,
                self.conv_out_channels,
                self.num_res_blocks,
                conv_cfg=self.conv_cfg,
                norm_cfg=self.norm_cfg)
