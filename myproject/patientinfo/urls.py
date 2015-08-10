from django.conf.urls import patterns, url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypatients/$', views.mypatients, name='mypatients'),
    url(r'^index_data/$', views.index_data, name='index_data'),
    url(r'^index_manage/$', views.index_manage, name='index_manage'),
    url(r'^(?P<patientinfo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<patientinfo_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<patientinfo_id>[0-9]+)/uploaddata/$', views.uploaddata, name='uploaddata'),
    url(r'^(?P<patientinfo_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<patientinfo_id>[0-9]+)/viewdata/$', views.viewdata, name='viewdata'),
]
