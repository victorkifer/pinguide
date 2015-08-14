from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('pinguide_web.urls')),
    url(r'^api/v1/', include('pinguide_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
