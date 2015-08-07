from django.conf.urls import patterns, url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<patientinfo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<patientinfo_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<patientinfo_id>[0-9]+)/uploaddata/$', views.uploaddata, name='uploaddata'),
    url(r'^(?P<patientinfo_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<patientinfo_id>[0-9]+)/viewdata/$', views.viewdata, name='viewdata'),
]
