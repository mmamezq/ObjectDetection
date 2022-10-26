"""

This is the script (in progress) used to run the training portion
from the command line

From terminal:

1. open virtual environment
2. Open mmdet_files directory
3. Run the following script

python tools/train.py configs/My_Config_Files/Quickrun2_TrainWithCustomizedDatasetConfig.py


"""

# The new config inherits a base config to highlight the necessary modification
_base_ = './mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('baby',)
data = dict(
    train=dict(
        img_prefix='../data/tao_train/frames/train',
        classes=classes,
        ann_file='../data/annotations/train_482_classes.json'))



# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = './checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'