#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ivydong
# @Date:   2015-07-26 01:33:33
# @Last Modified time: 2015-07-26 10:15:31

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^parse/$', views.parse_outtree, name='parse_outtree'),
	url(r'^$', views.index, name='index'),
]
