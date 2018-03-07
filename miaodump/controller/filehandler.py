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

    def readTxtToList(self,r_path):
        '''
        从txt文件逐行读取到list中
        :param r_path:
        :return:
        '''
        tmplist = []
        try:
            with open(r_path, 'r') as fp:
                fstr = fp.read()
                tmplist = re.findall(r'\w+', fstr)
                return tmplist
        except Exception, e:
            print e
            return tmplist

    def writeContextToFile(self,context, filepath):
        '''
        将内容写入文件
        :param context:
        :param filepath:
        :return:
        '''
        try:
            fwrite = open(filepath, 'w')
            fwrite.write(context)
        except Exception, e:
            print str(e)
            return False
        fwrite.close()

    def readContextFromFile(self,filepath):
        '''
        从文件读取内容
        :param filepath:
        :return:
        '''
        try:
            fread = open(filepath, 'r')
        except Exception, e:
            print str(e)
            return False
        tmpstr = fread.read()
        fread.close()
        return tmpstr

    def writeDictToHeaderFile(self, orig_dict, output_path):
        '''
        将字典键值对输出到一个header.h文件中
        :param orig_dict:
        :param output_path:
        :return:
        '''
        with open(output_path, 'w+') as fwrite:
            ctx_headers = config.HEADER_BANNER
            for (k,v) in orig_dict.iteritems():
                line_str = "#define %s %s" % (k, v)
                ctx_headers = ctx_headers + line_str
            ctx_headers = ctx_headers + config.HEADER_TAIL
            fwrite.write(ctx_headers)
        


