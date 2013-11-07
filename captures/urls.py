# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns("captures.views", url(r'^$', 'get_data', name='get-data'))
