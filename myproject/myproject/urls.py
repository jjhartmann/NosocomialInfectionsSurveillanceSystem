"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('index.urls', namespace='index')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/search/', include('basic_search.urls', namespace='basic_search')),
    url(r'^(?P<username>\w+)/', include('secure.urls', namespace='secure')),
    url(r'^(?P<username>\w+)/blast/', include('nocoblast.urls', namespace='nocoblast')),
    url(r'^(?P<username>\w+)/patientinfo/', include('patientinfo.urls', namespace='patientinfo')),
<<<<<<< HEAD
    url(r'^(?P<username>\w+)/graph/', include('graph.urls', namespace='graph')),
    url(r'^(?P<username>\w+)/search/details/matrix/', include('coc.urls', namespace='coc')),
=======
    url(r'^(?P<username>\w+)/userprofile/', include('userprofile.urls', namespace='userprofile')),
>>>>>>> ee61a3282f788a0559bab0441fab191abccfeaf1
]

