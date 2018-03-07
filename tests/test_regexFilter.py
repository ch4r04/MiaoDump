#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 10:36
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_regexFilter.py
from unittest import TestCase
from miaodump.controller.filter import RegexFilter


# @Software: PyCharm
class TestRegexFilter(TestCase):
    def test_getClsNameFromFilePath(self):
        fa = RegexFilter()
        print fa.getClsNameFromFilePath("/Users/ch4r0n/PycharmProjects/MiaoDump/miaodump/utils/AClass.h")

    def test_getMethodNameFromFilePath(self):
        fa = RegexFilter()
        print fa.getFuncNameFromFilePath("/Users/ch4r0n/PycharmProjects/MiaoDump/miaodump/utils/ViewController.m")

