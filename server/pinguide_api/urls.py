from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^recommend/(?P<token>\w{0,50})/$', views.recommend, name='recommend'),
]
