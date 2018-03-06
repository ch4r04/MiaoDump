#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 18:23
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_baseFilter.py
from unittest import TestCase
from miaodump.controller.filter import BaseFilter


# @Software: PyCharm
class TestBaseFilter(TestCase):

    def test_hmpchFilter(self):
        f = BaseFilter()
        print f.hmpchFilter("/Users/ch4r0n/Desktop/Rx_Swift_Leaning/MytestApp")
        pass

    def test_clsnameFilter(self):
        pass
