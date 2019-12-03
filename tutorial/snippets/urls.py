#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2019-12-03 10:37
# @Author   : yang.hong
# @FILE     : urls.py
# @Software : PyCharm

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^snippets/$', snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail)
]
