#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2019-12-03 10:37
# @Author   : yang.hong
# @FILE     : urls.py
# @Software : PyCharm

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
