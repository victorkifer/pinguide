CAFFE_DIR = '../scripts/caffe'

FOLDER_DATA = 'pinguide_logic/data'
FOLDER_MODEL = 'pinguide_logic/cache'
FOLDER_TMP = 'out'

INPUT_PINS = FOLDER_DATA + '/pins.sample.csv'
INPUT_USERS = FOLDER_DATA + '/users.sample.csv'
INPUT_IMAGES = FOLDER_DATA + '/pin_images.csv'
INPUT_REPINS = FOLDER_DATA + '/repins.train.csv'
INPUT_NEGATIVE_REPINS_TRAIN = FOLDER_DATA + '/repins.train.neg.csv'

OUTPUT_MODEL = FOLDER_MODEL + '/rfc_model.pkl'

# Recommend only images with positive probability higher that that value
POSITIVE_PREDICTION_RATE = 0.7
# Number of images that will be returned by recommender
RECOMMENDATION_LIST_SIZE = 80