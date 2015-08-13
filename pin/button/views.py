from django.shortcuts import render
from django import template
from django.template import loader
from django.template.loader import get_template 

def reg(request):
    template = loader.get_template('reg.html')
    return render(request, 'reg.html',{})

# Create your views here.
