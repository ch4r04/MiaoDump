#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 14:38
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_fileFilter.py
from unittest import TestCase
from miaodump.controller.filter import FileFilter
from miaodump.common.config import *


# @Software: PyCharm
class TestFileFilter(TestCase):
    def test_strContainFilter(self):
        file_path_list = ['/Users/ch4r0n/PycharmProjects/MiaoDump/miaodump/utils//AClass.h',
                          '/Users/ch4r0n/PycharmProjects/MiaoDump/miaodump/utils//ViewController.m']
        ff = FileFilter()
        print ff.strContainFilter(file_path_list, SDK_LIST)


class TestFileFilter(TestCase):
    def test_classdumpContextFromFiles(self):
        ff = FileFilter()
        ff.classdumpContextFromFiles("/Users/ch4r0n/Desktop/OFBank")

