__author__ = 'victor'

from rest_framework import serializers
from models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'img_id', 'url')