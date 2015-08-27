__author__ = 'viktor'

import numpy as np
import os
from pinguide_config import *
import glob
import time

import caffe

__CLASSIFIER = None

def init():
    __init_classifier()

def __init_classifier():
    model_def = CAFFE_DIR + '/models/bvlc_reference_caffenet/deploy.prototxt'
    pretrained_model = CAFFE_DIR + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
    mean_file = CAFFE_DIR + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'

    mean = np.load(mean_file).mean(1).mean(1)
    channel_swap = (2, 1, 0)
    raw_scale = 255.0
    # input_scale = 1.0
    image_dims = (256, 256)
    caffe.set_mode_cpu()

    classifier = caffe.Classifier(model_def, pretrained_model,
                                  mean=mean,
                                  channel_swap=channel_swap,
                                  raw_scale=raw_scale,
                                  image_dims=image_dims)

    global __CLASSIFIER
    __CLASSIFIER = classifier

def extract_for_dir(dir):
    input_file = os.path.expanduser(dir)
    ext = 'jpg'

    if __CLASSIFIER is None:
        __init_classifier()

    inputs = [caffe.io.load_image(im_f) for im_f in glob.glob(input_file + '/*.' + ext)]

    if len(inputs) == 0:
        raise AttributeError('No data found by given credentials')

    print("Classifying %d inputs." % len(inputs))

    # avg = [0.0 for i in range(1000)]
    # for image in inputs:
    #     prediction = __CLASSIFIER.predict([image])
    #     print prediction.shape
    #
    #     a = list(__CLASSIFIER.blobs['fc8'].data[4].flat)
    #     avg = [x + y for x, y in zip(avg, a)]
    #
    # count = len(inputs)
    # avg = [x / count for x in avg]

    prediction = __CLASSIFIER.predict(inputs)
    print prediction.shape

    # avg = list(__CLASSIFIER.blobs['fc8'].data[4].flat)
    #
    # a = list(__CLASSIFIER.blobs['fc7'].data[4].flat)
    # print len(a)
    # a = list(prediction[0]) + a
    # print len(a)

    avg = [0.0 for i in range(1000)]
    for line in prediction.tolist():
        avg = [x + y for x, y in zip(avg, line)]

    avg = [x / prediction.shape[0] for x in avg]

    return avg
