#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2020-01-07 16:57
# @Author   : yang.hong
# @FILE     : permissions.py
# @Software : PyCharm

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限：只允许对象的所有者编辑它。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 所以我们总是允许GET，HEAD 或 OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有改snippet的所有者才允许写权限。
        return obj.owner == request.user
