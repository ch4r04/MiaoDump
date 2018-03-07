#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:58
# @Author  : ch4r0n
# @Site    : 
# @File    : filter.py
# @Software: PyCharm

import os
import re

'''
文件类的Filter
'''
class FileFilter:

    def __init__(self):
        pass
    def hmmFilter(self, file_path):
        '''
        过滤.m .h 文件
        在同级目录遍历,查找到所有的文件
        传入参数:项目绝对路径
        :return: 文件的绝对路径列表，过滤完成
        '''
        mergelist = []
        for l in os.walk(file_path):
            # 过滤掉为空的列表
            if l[2]:
                # 组合列表 拼凑出绝对路径
                for absfile in l[2]:
                    mergelist.append(l[0] + '/' + absfile)
        mlist = []
        mmlist = []
        hlist = []
        for mstr in mergelist:
            if mstr.endswith('.m'):
                mlist.append(mstr)
            elif mstr.endswith('.h'):
                hlist.append(mstr)
            elif mstr.endswith('.mm'):
                mmlist.append(mstr)
        return [hlist, mlist, mmlist]

    def sdkFilter(self, orig_list, sdk_list):
        '''
        从原列表中过滤 使得不包含指定字符串(sdk_list)
        :param orig_list:
        :param sdk_list:
        :return:
        '''
        for i in orig_list:
            if i in sdk_list:
                orig_list.remove(i)
        return orig_list


class RegexFilter:

    def __init__(self):
        pass

    def getClsNameFromFilePath(self, file_path):
        '''
        从文件中获取类名
        :param file_path: 文件的绝对路径 一般是.h
        :return: 一个列表，包含多个类名
        '''
        with open(file_path, "r") as fopen:
            ctx = fopen.read()
            return re.findall(r'@interface\ (\w+)', ctx)

    def getFuncNameFromFilePath(self, file_path):
        '''
        从文件中获取方法名
        :param file_path:
        :return:
        '''
        with open(file_path, "r") as fopen:
            ctx = fopen.read()
            result = re.findall(r'(?:^|\n)([\-|\+].*)', ctx)
            flist = []
            for i in result:
                func_name = re.findall(r'\w+', i)[1]
                flist.append(func_name)
            return flist

















