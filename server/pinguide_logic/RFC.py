__author__ = 'victor'

import csv
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from logger import log

INPUT_FOLDER = 'pinguide_logic/data'
CACHE_FOLDER = 'pinguide_logic/cache'
INPUT_REPINS = INPUT_FOLDER + '/repins.train.csv'
INPUT_NEGATIVE_REPINS_TRAIN = INPUT_FOLDER + '/repins.train.neg.csv'
INPUT_PINS = INPUT_FOLDER + '/pins.sample.csv'
INPUT_USERS = INPUT_FOLDER + '/users.sample.csv'

__MODEL__ = None
__MODEL_FILE__ = CACHE_FOLDER + '/rfc_model.pkl'

def init():
  __loadModel()
  if __MODEL__ is None:
    __createModel()
    __saveModel()

def __loadModel():
  log('Loading RFC model')
  try:
    global __MODEL__
    __MODEL__ = joblib.load(__MODEL_FILE__)
  except IOError, e:
    print 'Cannot load model', e
  pass


def getModel():
  return __MODEL__


def __saveModel():
  log('Saving model for future use')
  if __MODEL__ is not None:
    joblib.dump(__MODEL__, __MODEL_FILE__)
    log('Model is saved')
  pass


def __createModel():
  log('Creating model from input data')

  log('Loading pins')
  m_pins = get_pins_map(INPUT_PINS)
  log('Loading users')
  m_users = get_users_map(INPUT_USERS)
  log('Loading positive repins')
  pos_repins = get_repins(INPUT_REPINS)
  log('Loading negative repins')
  neg_repins = get_repins(INPUT_NEGATIVE_REPINS_TRAIN)

  log('Preparing training data')
  x = []
  y = []

  for repin in pos_repins:
      if repin[0] not in m_users:
          continue
      if repin[1] not in m_pins:
          continue

      user_feature = m_users[repin[0]]
      pin_feature = m_pins[repin[1]]

      x.append(user_feature + pin_feature)
      y.append(1)

  for repin in neg_repins:
      if repin[0] not in m_users:
          continue
      if repin[1] not in m_pins:
          continue

      user_feature = m_users[repin[0]]
      pin_feature = m_pins[repin[1]]

      x.append(user_feature + pin_feature)
      y.append(0)

  m_pins = None
  m_users = None
  pos_repins = None
  neg_repins = None

  log('Start training')
  clf = RandomForestClassifier(n_estimators=10, n_jobs=4)
  clf.fit(x, y)

  global __MODEL__
  __MODEL__ = clf

  log('Model is created')
  pass


def get_pins_map(file):
  '''
  Returns pins map
  key = pin_id
  value = pin_features
  '''
  pins = {}
  with open(file, 'rb') as f_pins:
    reader = csv.reader(f_pins, delimiter='|')
    for row in reader:
      pins[int(row[0])] = [float(x) for x in row[1:1015]]
  return pins

def get_users_map(file):
    '''
    Returns users map
    key = user_id
    value = user_features
    '''
    users = {}
    with open(file, 'rb') as f_users:
        reader = csv.reader(f_users, delimiter='|')
        for row in reader:
            users[int(row[0])] = [float(x) for x in row[1:]]
    return users

def get_repins(file):
    '''
    Returns all repins from given file
    Repin is represented as a tuple (user_id, pin_id)
    '''
    repins = []
    with open(file, 'rb') as repins_file:
        reader = csv.reader(repins_file, delimiter='|')
        for row in reader:
            repins.append((int(row[0]), int(row[1])))
    return repins