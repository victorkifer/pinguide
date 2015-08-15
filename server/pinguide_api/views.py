import json
from django.http import HttpResponse

from models import *


def index(req):
  return HttpResponse("PinGuide API")


def recommend(req):
  nickname = req.GET.get('nickname', None)
  board_id = req.GET.get('board_id', None)

  response = None
  if nickname is None or board_id is None:
    response = {
      'status': -1,
      'error': 'Required fields: nickname, board_id'
    }
  else:
    images = Image.objects.all()[:20]
    json_data = [image.as_json() for image in images]

    response = {
      'status': 0,
      'data': json_data
    }

  return HttpResponse(json.dumps(response), content_type='json')
