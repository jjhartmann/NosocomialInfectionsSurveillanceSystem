__author__ = 'Jeremy'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.indexView, name='index'),
    url(r'^details/$', views.process_search, name='details')
]

