from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'^setprofile/$', views.set_profile, name='setprofile'),
	url(r'^viewprofile/$', views.view_profile, name='viewprofile'),
]