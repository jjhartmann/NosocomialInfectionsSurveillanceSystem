__author__ = 'Jeremy'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.indexview, name='index'),
]

