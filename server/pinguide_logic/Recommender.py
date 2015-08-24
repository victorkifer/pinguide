__author__ = 'victor'

from pinguide_config import *
from pinguide_api.models import *

import Downloader
import Extractor
import RFC
import operator

def recommend(nickname, board_name):
    # downloading images
    __download_images(nickname, board_name)

    # extracting average user features
    downloads_dir = __get_downloads_dir(nickname, board_name)
    user_features = __extract_average_user_features(downloads_dir)

    # loading pins for prediction
    keys, values = __get_pins()

    # predicting
    y = __predict_for(user_features, values)

    # leaving only pins with probability > POSITIVE_PREDICTION_RATE
    # and sort pins by probability from higher to lower
    y = __filter_and_sort_by_probability(y, POSITIVE_PREDICTION_RATE)

    # get image ids for pins with high predictions (y)
    image_ids = __get_image_ids(keys, y)

    # get images by ids, but limit number of images by RECOMMENDATION_LIST_SIZE
    selected = __get_images_by_ids(image_ids, RECOMMENDATION_LIST_SIZE)

    return selected

def __download_images(nickname, board_name):
    Downloader.fetch_images(nickname, board_name)
    print 'Images downloaded'

def __get_downloads_dir(nickname, board_name):
    return Downloader.get_dir(nickname, board_name)

def __extract_average_user_features(dir):
    user_features = Extractor.extract_for_dir(dir)
    print 'User features extracted'
    return user_features

def __get_pins():
    keys, values = RFC.getRandomPins(10000)
    print 'Random images received'
    return keys, values

def __predict_for(user_features, pins_values):
    x = __format_set_for_prediction(user_features, pins_values)
    y = RFC.getModel().predict_proba(x)
    print 'Prediction for random images computed'
    return [z.tolist() for z in y]

def __format_set_for_prediction(user_features, pins_values):
    x = []
    for value in pins_values:
        x.append(user_features + value)
    return x

def __filter_and_sort_by_probability(y, filter_min_probability):
    for i in range(len(y)):
        y[i].insert(0, i)

    col_pos_predict = RFC.getModel().classes_.tolist().index(1) + 1
    y = [z for z in y if z[col_pos_predict] >= filter_min_probability]

    y.sort(key=operator.itemgetter(col_pos_predict), reverse=True)

    return y

def __get_image_ids(keys, y):
    image_ids = []
    for i in range(len(y)):
        image_ids.append(keys[y[i][0]])

    print 'Recommended image ids founded', len(image_ids)
    return image_ids

def __get_images_by_ids(image_ids, limit):
    selected = []
    for image_id in image_ids:
        image = Image.objects.get(pk=image_id)

        if image is not None:
            selected.append(image)

            if len(selected) == limit:
                break

    return selected