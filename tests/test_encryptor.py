#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 16:07
# @Author  : ch4r0n
# @Site    : ${SITE}
# @File    : test_encryptor.py
from unittest import TestCase
from miaodump.controller.encryptor import Encryptor


# @Software: PyCharm
class TestEncryptor(TestCase):
    def test_secKeyCreate(self):
        alist = ["AAA","HDKJF","BClass"]
        enc = Encryptor()
        print enc.secKeyCreate(alist)


