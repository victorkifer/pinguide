__author__ = 'viktor'

import numpy as np
import os
from pinguide_config import *
import glob
import time

import caffe

__CLASSIFIER = None

def __init_classifier():
    model_def = CAFFE_DIR + '/models/bvlc_reference_caffenet/deploy.prototxt'
    pretrained_model = CAFFE_DIR + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
    mean_file = CAFFE_DIR + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'
    channel_swap_data = '2,1,0'
    input_scale = 1.0
    raw_scale = 255.0
    images_dim = '256,256'
    caffe.set_mode_cpu()
    print("CPU mode")

    image_dims = [int(s) for s in images_dim.split(',')]

    mean, channel_swap = None, None
    if mean_file:
        mean = np.load(mean_file).mean(1).mean(1)
    if channel_swap_data:
        channel_swap = [int(s) for s in channel_swap_data.split(',')]

    classifier = caffe.Classifier(model_def, pretrained_model,
            image_dims=image_dims, mean=mean,
            input_scale=input_scale, raw_scale=raw_scale,
            channel_swap=channel_swap)

    global __CLASSIFIER
    __CLASSIFIER = classifier

def extract_for_dir(dir):
    input_file = os.path.expanduser(dir)
    output_file = dir + 'output.npy'
    ext = 'jpg'

    if __CLASSIFIER is None:
        __init_classifier()

    center_only = False

    # Load numpy array (.npy), directory glob (*.jpg), or image file.
    if input_file.endswith('npy'):
        print("Loading file: %s" % input_file)
        inputs = np.load(input_file)
    elif os.path.isdir(input_file):
        print("Loading folder: %s" % input_file)
        inputs =[caffe.io.load_image(im_f)
                 for im_f in glob.glob(input_file + '/*.' + ext)]
    else:
        print("Loading file: %s" % input_file)
        inputs = [caffe.io.load_image(input_file)]

    print("Classifying %d inputs." % len(inputs))

    # Classify.
    start = time.time()
    predictions = __CLASSIFIER.predict(inputs, not center_only)
    print("Done in %.2f s." % (time.time() - start))

    return predictions
