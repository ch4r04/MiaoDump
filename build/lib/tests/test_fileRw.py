#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 11:52
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_fileRw.py
from unittest import TestCase
from miaodump.controller.filehandler import FileRw
from miaodump.common import config

# @Software: PyCharm
class TestFileRw(TestCase):
    def test_readTxtToList(self):
        filerw = FileRw()
        a = filerw.readTxtToList("/Users/ch4r0n/PycharmProjects/MiaoDump/miaodump/utils/reskeys.txt")

    def test_writeContextToFile(self):
        pass

    def test_readContextFromFile(self):
        pass

    def test_writeDictToHeaderFile(self):
        filerw = FileRw()
        filerw.writeDictToHeaderFile({"aaa":"alksdjflksdjf"}, "./headers.h")


