import json
import sys
from django.http import HttpResponse

from models import *

sys.path.append('..')
from pinguide_logic import Downloader

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
    Downloader.fetch_images(nickname, board_name)
    dir = Downloader.get_dir(nickname, board_name)

    images = Image.objects.all()[:20]
    json_data = [image.as_json() for image in images]

    response = {
      'status': 0,
      'data': json_data
    }

  return HttpResponse(json.dumps(response), content_type='json')
