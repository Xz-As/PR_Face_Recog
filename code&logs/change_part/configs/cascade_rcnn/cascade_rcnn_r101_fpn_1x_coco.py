_base_ = './cascade_rcnn_r50_fpn_1x_coco.py'
model = dict(
    #pretrained='open-mmlab://detectron2/resnet101',
    backbone=dict(depth=101))
