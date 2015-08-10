__author__ = 'Jeremy'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.indexview, name='index'),
    url(r'^gen/(?P<id>[0-9]+)/$', views.generate, name='generate'),
    url(r'^gen2/(?P<id>[0-9]+)/$', views.generate2, name='generate2'),
]

