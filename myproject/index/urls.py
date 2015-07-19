__author__ = 'Jeremy'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexview, name='index'),  # main index page.
    # url(r'^about/'), # about page.
    # url(r'^features/'), # features page.
    # url(r'^login/'), #login page
]