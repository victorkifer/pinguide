import json
from django.http import HttpResponse

from models import *


def index(req):
  return HttpResponse("PinGuide API")


def recommend(req, token):
  images = Image.objects.all()[:20]
  json_data = [image.as_json() for image in images]

  response = {
    'status': 0,
    'data': json_data
  }
  return HttpResponse(json.dumps(response), content_type='json')
