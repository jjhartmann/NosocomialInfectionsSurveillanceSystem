#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ivydong
# @Date:   2015-07-26 03:02:55
# @Last Modified time: 2015-07-27 11:43:13

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^parse/$', views.parse_data, name='parse_data'),
]