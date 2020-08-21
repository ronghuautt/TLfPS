#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:04:03 2019

@author: hu
"""
import numpy as np

class Config(object):
    def __init__(self, M):
        assert M in ['mrcnn', 'yolov3', 'yolov4', 'oim']
        #configuration for the detectors
        self.M = M
        if M == 'mrcnn':
            self.BACKBONE = "resnet101"
            self.TOP_DOWN_PYRAMID_SIZE = 256
            self.TRAIN_BN = False
            self.POOL_SIZE = 7
            self.FC_SIZE = 520
            self.IMAGE_SIZE = [1024, 1024]
            self.IMAGE_RESIZE_MODE = "square"
            self.IMAGE_MIN_DIM = 800
            self.IMAGE_MAX_DIM = 1024
            self.IMAGE_MIN_SCALE = 0
            self.MEAN_PIXEL = np.array([123.7, 116.8, 103.9])
            self.RPN_BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
            self.BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
            self.GT_VR_THRESHOLD = 0.9
            self.IMAGE_META_SIZE = 1 + 3 + 3 + 4 + 1 + 81
            self.RPN_ANCHOR_RATIOS = [0.5, 1, 2]
            self.RPN_ANCHOR_STRIDE = 1
            self.RPN_NMS_THRESHOLD = 0.7
            self.RPN_ANCHOR_SCALES = (32, 64, 128, 256, 512)
            self.BACKBONE_STRIDES = [4, 8, 16, 32, 64]
            self.POST_NMS_ROIS_INFERENCE = 1000
            self.DETECTION_MIN_CONFIDENCE = 0.90
            self.DETECTION_NMS_THRESHOLD = 0.3
            self.DETECTION_MAX_INSTANCES = 100
            self.PRE_NMS_LIMIT = 6000
            self.IMAGES_PER_GPU = 1
            self.layer = 1
            self.SEnet = True
            self.sim_type = ['cosine', 'l2norm_cosine', 'l2norm', 'theta'][0]
            self.l2_norm = self.sim_type != 'l2norm'
        elif M == 'yolov3':
            self.MEAN_PIXEL = np.array([0, 0, 0])
            self.IMAGE_SIZE = [416, 416]
            self.IMAGE_MAX_DIM = 416
            self.IMAGE_MIN_DIM = 384
            self.DETECTION_MIN_CONFIDENCE = 0.3
            self.DETECTION_NMS_THRESHOLD = 0.3
            self.YOLO_NUM_ANCHORS = 3
            self.YOLO_NUM_CLASSES = 80
            self.anchors = [[[10, 13], [16,  30], [33,  23]], [[30, 61], [62,  45], [59, 119]], [[116,90], [156,198], [373,326]]]
            self.layer = 1
            self.SEnet = True
            self.sim_type = ['cosine', 'l2norm_cosine', 'l2norm', 'theta'][2]
            self.l2_norm = self.sim_type != 'l2norm'
        elif M == 'yolov4':
            self.MEAN_PIXEL = np.array([0, 0, 0])
            self.IMAGE_SIZE = [608, 608]
            self.IMAGE_MAX_DIM = 608
            self.IMAGE_MIN_DIM = 578
            self.DETECTION_MIN_CONFIDENCE = 0.5
            self.DETECTION_NMS_THRESHOLD = 0.45
            self.YOLO_NUM_ANCHORS = 3
            self.YOLO_NUM_CLASSES = 80
            self.anchors = [[[12, 16], [19, 36], [40, 28]], [[36, 75], [76, 55], [72, 146]], [[142, 110], [192, 243], [459, 401]]]
            self.layer = 1
            self.SEnet = True
            self.sim_type = ['cosine', 'l2norm_cosine', 'l2norm', 'theta'][0]
            self.l2_norm = self.sim_type != 'l2norm'
        elif M == 'oim': #unsupported
            self.MEAN_PIXEL = np.array([102.9801, 115.9465, 122.7717])
            self.IMAGE_SIZE = [600, 600]
            self.IMAGE_MAX_DIM = 600
            self.IMAGE_RESIZE_MODE = "square"
            self.IMAGE_MIN_SCALE = 0
            self.layer = 0
            self.sim_type = ['cosine', 'l2norm_cosine', 'l2norm', 'theta'][0]
        else:
            raise ValueError('unsupported type...')
        self.NUM_CLASSES = 81
        self.BATCH_SIZE = 6
        self.DEBUG = False
        self.MAX_INTERVAL = 80
        self.MAX_TRACKING_VOLUME = 35
        self.MIN_VR = 0.4
        self.MAX_OFFSET_LEN = 0.1
        self.POOL_SIZE = 7
        self.IMAGE_RESIZE_MODE = "square"
        self.IMAGE_MIN_SCALE = 0
        self.DEBUG = False
        self.BATCH_SIZE = 6
        self.FC_SIZE = 1024
        self.TRAIN_BN = False
        self.FL = 256
        self.FN = 6
        self.DTABLE_SIZE = 5000
        self.max_volume = 8
        self.mgn = True
        self.mosaicSize = 4