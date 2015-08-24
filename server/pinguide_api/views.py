import json
from django.http import HttpResponse

from models import *

from pinguide_logic import Recommender,Downloader
from pinguide_config import *
import operator

def index(req):
  return HttpResponse("PinGuide API")


def prepare(req):
  import csv

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
      recommended = Recommender.recommend(nickname, board_name)

      json_data = [image.as_json() for image in recommended]

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
