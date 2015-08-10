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

from basic_search.models import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Influenza_NA
        fields = ('completeness', 'virus_name', 'date_discovered', 'age', 'genomesegment_or_proteinname' , 'subtype', 'host', 'gender', 'sequence_length', 'genbank_accession_number')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Influenza_NA.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'nocoapi', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    url(r'^', include('index.urls', namespace='index')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/search/', include('basic_search.urls', namespace='basic_search')),
    url(r'^(?P<username>\w+)/', include('secure.urls', namespace='secure')),
    url(r'^(?P<username>\w+)/blast/', include('nocoblast.urls', namespace='nocoblast')),
    url(r'^(?P<username>\w+)/patientinfo/', include('patientinfo.urls', namespace='patientinfo')),
    url(r'^(?P<username>\w+)/graph/', include('graph.urls', namespace='graph')),
    url(r'^(?P<username>\w+)/search/details/matrix/', include('coc.urls', namespace='coc')),
    url(r'^(?P<username>\w+)/userprofile/', include('userprofile.urls', namespace='userprofile')),
    url(r'^(?P<username>\w+)/phylo/', include('treebuilder.urls', namespace='phylo')),
  
]

