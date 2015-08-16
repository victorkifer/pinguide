import json
from django.http import HttpResponse

from models import *

from pinguide_logic import Downloader,Extractor

def index(req):
  return HttpResponse("PinGuide API")


def recommend(req):
  nickname = req.GET.get('nickname', None)
  board_name = req.GET.get('board_name', None)

  response = None
  if nickname is None or board_name is None:
    response = {
      'status': -1,
      'error': 'Required fields: nickname, board_id'
    }
  else:
    response = None
    try:
      Downloader.fetch_images(nickname, board_name)
      dir = Downloader.get_dir(nickname, board_name)

      Extractor.extract_for_dir(dir)

      images = Image.objects.all()[:20]
      json_data = [image.as_json() for image in images]

      response = {
        'status': 0,
        'data': json_data
      }
    except IOError as e:
      response = {
        'status': 500,
        'error': e.strerror
      }
      print e

  return HttpResponse(json.dumps(response), content_type='json')
