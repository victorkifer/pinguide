from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^prepare/$', views.prepare, name='prepare'),
   url(r'^recommend/$', views.recommend, name='recommend'),
]
