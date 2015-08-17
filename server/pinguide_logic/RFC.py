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

__M_PINS = None
__MODEL__ = None
__MODEL_FILE__ = CACHE_FOLDER + '/rfc_model.pkl'

__FEATURES_FIRST = 15
__FEATURES_LAST = 1015
__FEATURES_COUNT = __FEATURES_LAST - __FEATURES_FIRST

def init():
  global __M_PINS
  log('Loading pins')
  __M_PINS = get_pins_map(INPUT_PINS)

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

def getRandomPins(count):
  selected = []
  selected_keys = []
  keys = list(__M_PINS.keys())

  if len(keys) < count:
    raise AttributeError('count is more than images available')

  while len(selected) < count:
    from random import random
    key = keys[int(random() % len(keys))]
    keys.remove(key)

    selected.append(__M_PINS[key])
    selected_keys.append(key)

  return selected_keys, selected

def __saveModel():
  log('Saving model for future use')
  if __MODEL__ is not None:
    joblib.dump(__MODEL__, __MODEL_FILE__)
    log('Model is saved')
  pass


def __createModel():
  log('Creating model from input data')

  m_pins = __M_PINS
  log('Loading positive repins')
  pos_repins = get_user_repins_map(INPUT_REPINS)
  log('Loading negative repins')
  neg_repins = get_user_repins_map(INPUT_NEGATIVE_REPINS_TRAIN)

  log('Preparing training data')
  x = []
  y = []

  for user_id in pos_repins.keys():
    pins = pos_repins[user_id]

    count = len(pins)
    if count <= 0:
      continue

    avg = [0 for i in range(__FEATURES_COUNT)]
    for pin_id in pins:
      if pin_id not in m_pins.keys():
        continue

      pin = m_pins[pin_id]

      for i in range(__FEATURES_COUNT):
        avg[i] += pin[i]

    avg = [z * 1.0 / count for z in avg]

    for pin_id in pins:
      if pin_id not in m_pins.keys():
        continue

      pin = m_pins[pin_id]

      x.append(avg + pin)
      y.append(1)

    if user_id not in neg_repins.keys():
      continue

    pins = neg_repins[user_id]
    for pin_id in pins:
      if pin_id not in m_pins.keys():
        continue

      pin = m_pins[pin_id]

      x.append(avg + pin)
      y.append(0)

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
      pins[int(row[0])] = [float(x) for x in row[__FEATURES_FIRST:__FEATURES_LAST]]
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


def get_user_repins_map(file):
  '''
  Returns all repins from given file
  Repin is represented as a tuple (user_id, pin_id)
  '''
  repins = {}
  with open(file, 'rb') as repins_file:
    reader = csv.reader(repins_file, delimiter='|')
    for row in reader:
      user_id = int(row[0])
      pin_id = int(row[1])
      if int(row[0]) not in repins.keys():
        repins[user_id] = [pin_id]
      else:
        repins[user_id].append(pin_id)
  return repins
