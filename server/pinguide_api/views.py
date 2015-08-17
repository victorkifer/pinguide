import json
from django.http import HttpResponse

from models import *

from pinguide_logic import Downloader,Extractor,RFC

def index(req):
  return HttpResponse("PinGuide API")


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

      keys, values = RFC.getRandomPins(1000)
      print 'Random images received'

      x = []
      for value in values:
        x.append(user_features + value)

      y = RFC.getModel().predict(x)
      print 'Prediction for random images computed'

      image_ids = set()
      for i in range(len(y)):
        if y[i] == 1:
          image_ids.add(keys[i])

      print 'Recommended image ids founded', len(image_ids)

      images = Image.objects.all()

      selected = []
      for image in images:
        if image.img_id in image_ids:
          selected.append(image)

          if len(selected) == 20:
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
