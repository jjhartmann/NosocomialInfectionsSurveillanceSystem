__author__ = 'Jeremy'


from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.indexView, name='index'),
    url(r'^process/$', views.process_search, name='process')
]