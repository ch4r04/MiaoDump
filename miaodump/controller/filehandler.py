#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:48
# @Author  : ch4r0n
# @Site    : 
# @File    : filehandler.py
# @Software: PyCharm

from ..common import config
import re

class FileRw:

    def __init__(self):
        pass
    # 从文件中逐行读取到列表
    def readTxtToList(self,r_path):
        tmplist = []
        try:
            with open(r_path, 'r') as fp:
                fstr = fp.read()
                tmplist = re.findall(r'\w+', fstr)
                return tmplist
        except Exception, e:
            print e
            return tmplist

    # 内容写入文件操作
    def writeContextToFile(self,context, filepath):
        try:
            fwrite = open(filepath, 'w')
            fwrite.write(context)
        except Exception, e:
            print str(e)
            return False
        fwrite.close()

    # 从文件读取内容操作
    # 返回值:文件内容串
    def readContextFromFile(self,filepath):
        try:
            fread = open(filepath, 'r')
        except Exception, e:
            print str(e)
            return False
        tmpstr = fread.read()
        fread.close()
        return tmpstr







