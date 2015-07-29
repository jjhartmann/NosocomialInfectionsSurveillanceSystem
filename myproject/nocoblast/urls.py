from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',

    url(r'^blastn/', views.blastn, name="blastn"),
    url(r'^tblastn/', views.tblastn, name="tblastn"),
    url(r'^blast/$', views.blastn),
)
