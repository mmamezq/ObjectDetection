# Copyright (c) OpenMMLab. All rights reserved.

"""
This tutorial uses the computer's webcam and
an rcnn model to perform inference on each frame.
As we can see, the accuracy of some of the detected
objects is not accurate.

The code modifies the webcam_demo.py found under
mmdet_files/demo/webcam_demo.py

as well as information from the following link:
https://mmdetection.readthedocs.io/en/stable/1_exist_data_model.html
"""

import argparse

import cv2
import torch
from mmdet.apis import inference_detector, init_detector
from matplotlib import pyplot as plt


config_file = '../mmdet_files/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = '../mmdet_files/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
device = 'cuda:0'

model = init_detector(config_file, checkpoint_file, device=device)

camera = cv2.VideoCapture(0)

counter = 10;

while True:
    ret_val, img = camera.read()
    result = inference_detector(model, img)
    ch = cv2.waitKey(1)
    if ch == 27 or ch == ord('q') or ch == ord('Q'):
        break
    model.show_result(img, result, score_thr=.3, wait_time=1, show=True)
    counter -= 1