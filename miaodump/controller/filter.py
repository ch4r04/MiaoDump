#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:58
# @Author  : ch4r0n
# @Site    : 
# @File    : filter.py
# @Software: PyCharm

import os

class BaseFilter:

    def __init__(self):
        pass

    def hmpchFilter(self, file_path):
        '''
        过滤.m .h .pch文件
        在同级目录遍历,查找到所有的文件
        传入参数:项目绝对路径
        :return: 文件的绝对路径列表，过滤完成
        '''
        mergelist = []
        for list in os.walk(file_path):
            # 过滤掉为空的列表
            if list[2] != []:
                # 组合列表 拼凑出绝对路径
                for absfile in list[2]:
                    mergelist.append(list[0] + '/' + absfile)
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

    def clsnameFilter(self,file_list):
        '''
        从文件中获取到所有的类名
        :param file_list:
        :return:
        '''
        pass


