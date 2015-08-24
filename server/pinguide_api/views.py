import json
from django.http import HttpResponse

from models import *

from pinguide_logic import Downloader,Extractor,RFC
from pinguide_config import *
import operator

def index(req):
  return HttpResponse("PinGuide API")


def prepare(req):
  import csv

  INPUT_FOLDER = 'pinguide_logic/data'
  INPUT_IMAGES = INPUT_FOLDER + '/pin_images.csv'

  with open(INPUT_IMAGES, 'rb') as f_pins:
      reader = csv.reader(f_pins, delimiter='|')
      for row in reader:
          img_id = int(row[0])
          url = row[1]

          image = Image(id=img_id, url=url)
          image.save()

  return HttpResponse("Done")

def recommend(req):
  nickname = req.GET.get('nickname', None)
  board_name = req.GET.get('board_name', None)

  response = None
  if nickname is None or board_name is None:
    print 'No data'
    response = {
      'status': -1,
      'error': 'Required fields: nickname, board_name'
    }
  else:
    try:
      Downloader.fetch_images(nickname, board_name)
      dir = Downloader.get_dir(nickname, board_name)
      print 'Images downloaded'

      user_features = Extractor.extract_for_dir(dir)
      print 'User features extracted'

      keys, values = RFC.getRandomPins(10000)
      print 'Random images received'

      x = []
      for value in values:
        x.append(user_features + value)

      y = RFC.getModel().predict_proba(x)
      print 'Prediction for random images computed'

      y = [z.tolist() for z in y]

      for i in range(len(y)):
        y[i].insert(0, i)

      col_pos_predict = RFC.getModel().classes_.tolist().index(1) + 1
      y = [z for z in y if z[col_pos_predict] >= POSITIVE_PREDICTION_RATE]

      y.sort(key=operator.itemgetter(col_pos_predict), reverse=True)

      image_ids = set()
      for i in range(len(y)):
        image_ids.add(keys[y[i][0]])

      print 'Recommended image ids founded', len(image_ids)

      images = Image.objects.all()

      selected = []
      for image in images:
        if image.id in image_ids:
          selected.append(image)

          if len(selected) == RECOMMENDATION_LIST_SIZE:
            break

      json_data = [image.as_json() for image in selected]

      response = {
        'status': 0,
        'data': json_data
      }
    except BaseException as e:
      response = {
        'status': 500,
        'error': str(e)
      }
    finally:
      Downloader.remove_download(nickname, board_name)

  return HttpResponse(json.dumps(response), content_type='json')
