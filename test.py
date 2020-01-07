#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2020-01-07 16:03
# @Author   : yang.hong
# @FILE     : test.py
# @Software : PyCharm


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)
