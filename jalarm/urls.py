# coding:utf-8
from django.conf.urls import patterns, include, url
from jalarm.views import *

urlpatterns = patterns('',
                       url(r'^list/(\w+)/$', log_alarm, name='log_alarm'),
                       )
