_base_ = '../cascade_rcnn/cascade_rcnn_r101_giou_fpn_1x_voc.py'
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)))
