__author__ = 'Jeremy'


from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]