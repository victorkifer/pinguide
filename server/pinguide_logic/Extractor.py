__author__ = 'viktor'

import numpy as np
import os
from pinguide_config import *
import glob
import time

import caffe

__CLASSIFIER = None
__TRANSFORMER = None

def init():
    __init_classifier()

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

    classifier = caffe.Net(model_def, pretrained_model, caffe.TEST)

    transformer = caffe.io.Transformer({'data': classifier.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_mean('data', mean) # mean pixel
    transformer.set_raw_scale('data', raw_scale)  # the reference model operates on images in [0,255] range instead of [0,1]
    transformer.set_channel_swap('data', channel_swap)  # the reference model has channels in BGR order instead of RGB

    global __CLASSIFIER
    __CLASSIFIER = classifier

    global __TRANSFORMER
    __TRANSFORMER = transformer

def extract_for_dir(dir):
    input_file = os.path.expanduser(dir)
    ext = 'jpg'

    if __CLASSIFIER is None:
        __init_classifier()

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

    __CLASSIFIER.blobs['data'].reshape(50, 3, 227, 227)

    # features = []
    processed_inputs = []
    for input in inputs:
        processed_inputs.append(__TRANSFORMER.preprocess('data', input))

    __CLASSIFIER.forward_all(data=np.array(processed_inputs))

    # __CLASSIFIER.blobs['data'].data[...] = __TRANSFORMER.preprocess('data', input)
    #   __CLASSIFIER.forward()
    #
    #   features.append(__CLASSIFIER.blobs['fc8'].data[0].tolist())


    return __CLASSIFIER.blobs['fc8'].data[0].tolist()
    # Classify.
    # start = time.time()
    # predictions = __CLASSIFIER.predict(inputs, not center_only)
    # print("Done in %.2f s." % (time.time() - start))

    # return predictions
