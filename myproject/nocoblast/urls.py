from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',

    url(r'^blastn/', views.blastn),
    url(r'^tblastn/', views.tblastn),
    url(r'^blast/$', views.blastn),
)
