"""
This script uses a pretrained faster_rcnn model to inference on
images from Tao_train dataset

We inference on an image first then a video frame by frame

This tutorial follows the information from the following link:
https://mmdetection.readthedocs.io/en/stable/1_exist_data_model.html
"""
from mmdet.apis import init_detector, inference_detector
import mmcv
import matplotlib.pyplot as plt
# Specify the path to model config and checkpoint file
config_file = '../mmdet_files/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = '../mmdet_files/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = '../data/tao_train/frames/train/YFCC100M/v_3d84802a7129a8649f38d2bcf2debc3/frame0302.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# visualize the results in a new window
model.show_result(img, result,show=True)

"""
# test a video and show the results
video = mmcv.VideoReader('mmdet_files/demo/demo.mp4')
for frame in video:
    result = inference_detector(model, frame)
    val = model.show_result(frame, result)
    plt.imshow(val)
    plt.show()
"""