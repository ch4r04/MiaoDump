#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 18:23
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_baseFilter.py
from unittest import TestCase
from miaodump.controller.filter import FileFilter


# @Software: PyCharm
class TestBaseFilter(TestCase):

    def test_hmpchFilter(self):
        f = FileFilter()
        print f.hmmFilter("/Users/ch4r0n/Desktop/Rx_Swift_Leaning/MytestApp")
        pass

    def test_clsnameFilter(self):
        pass

    def test_sdkFilter(self):
        f = FileFilter()
        orig_list  = ['AAA','BBB','CCC']
        white_list = ['AAA', '123123k']
        print f.sdkFilter(orig_list, white_list)


