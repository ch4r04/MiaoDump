#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 12:07
# @Author  : ch4r0n
# @Site    : 
# @File    : miaodump_converter.py
# @Software: PyCharm
import os
from miaodump.controller.filter import *
from miaodump.common.config import *
from miaodump.controller.filehandler import *
from miaodump.controller.encryptor import *
import struct


class MiaodumpConverter:
    """Top level converter class."""

    def __init__(self, **kwargs):
        self.file_path = kwargs.get('file_path', None)
        self.exclude = kwargs.get('exclude', None)
        self.default_exclude = kwargs.get('default_exclude', None)
        self.arch = kwargs.get('arch', None)
        self.output = kwargs.get('output', None)

        # verify file path
        if not os.path.exists(self.file_path):
            print("Couldn't open the path: %s" % self.file_path)
            return

        # verify output file
        if not os.path.exists(self.output):
            print("Couldn't write the header to path: %s" % self.output)
            return
        self.run(self.arch)

    def run(self, arch_type):
        # run not use class_dump
        if not arch_type:
            try:
                exc_list = []
                if self.exclude:
                    exc_tmp_list = self.exclude.split(',')
                    for i in exc_tmp_list:
                        exc_list.append(i.strip())

                file_filter = FileFilter()
                cmmp_files = file_filter.hmmFilter(self.file_path)

                # filter exclude sdk default
                if self.default_exclude:
                    cmmp_files = file_filter.strContainFilter(cmmp_files, SDK_LIST)

                # filter exclude sdk
                if self.exclude:
                    cmmp_files = file_filter.strContainFilter(cmmp_files, exc_list)

                reg_filter = RegexFilter()
                cls_h, func_m = file_filter.seprateHandMfromFiles(cmmp_files)
                cls_names = reg_filter.getClsNameFromHeaderList(cls_h)
                func_names = reg_filter.getFuncNameFromMMList(func_m)
                all_keywords = cls_names + func_names

                # filter  reskeys.txt
                fw = FileRw()
                res_list = fw.readTxtToList(RES_KEY_PATH)
                filter_result = file_filter.strMatchFilter(all_keywords, res_list)
                print(filter_result)

                encryptor = Encryptor()
                enc_key_value = encryptor.secKeyCreate(filter_result)
                fw.writeDictToHeaderFile(enc_key_value, self.output)
            except Exception, e:
                print(e)
                return
        else:
            print("use class-dump")
            # verify the file is a binary files
            try:
                ff = FileFilter()
                cls_dump_result = ff.classdumpContextFromFiles(self.file_path)
                reg_filter = RegexFilter()
                all_keywords = reg_filter.getClsAndFuncFromContext(cls_dump_result)
                if not all_keywords:
                    return
                
                fw = FileRw()
                res_list = fw.readTxtToList(RES_KEY_PATH)
                filter_result = ff.strMatchFilter(all_keywords, res_list)
                # encryptor
                encryptor = Encryptor()
                enc_key_value = encryptor.secKeyCreate(filter_result)
                fw.writeDictToHeaderFile(enc_key_value, self.output)
            except Exception, e:
                print(e)
                pass
