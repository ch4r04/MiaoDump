#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 17:39
# @Author  : ch4r0n
# @Site    : 
# @File    : cmdline.py
# @Software: PyCharm

import argparse
from miaodump.common import config

class ArgParse:

    def __init__(self, **kwargs):
        self.file_path = kwargs.get('file_path', None)
        self.exclude = kwargs.get('exclude', None)
        self.default_exclude = kwargs.get('default_exclude', None)
        self.arch = kwargs.get('arch', None)
        self.output = kwargs.get('output',None)



    def startCMDLine(self):
        pass

