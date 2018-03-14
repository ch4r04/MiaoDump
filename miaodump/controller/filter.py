#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:58
# @Author  : ch4r0n
# @Site    : 
# @File    : filter.py
# @Software: PyCharm

import os
import re
import commands
import struct

'''
文件类的Filter
'''


class FileFilter:

    def __init__(self):
        pass


    # 字节码转16进制字符串
    def bytes2hex(self,bytes):
        num = len(bytes)
        hexstr = u""
        for i in range(num):
            t = u"%x" % bytes[i]
            if len(t) % 2:
                hexstr += u"0"
            hexstr += t
        return hexstr.upper()

    def hmmFilter(self, file_path):
        '''
        过滤.m .h 文件
        在同级目录遍历,查找到所有的文件
        传入参数:项目绝对路径
        :return: 文件的绝对路径列表，过滤完成
        '''
        if not os.path.exists(file_path):
            return None
        mergelist = []
        for l in os.walk(file_path):
            # 过滤掉为空的列表
            if l[2]:
                # 组合列表 拼凑出绝对路径
                for absfile in l[2]:
                    mergelist.append(l[0] + '/' + absfile)
        all_list = []
        for mstr in mergelist:
            if mstr.endswith('.m') or mstr.endswith(".h") or mstr.endswith(".mm"):
                all_list.append(mstr)
        return all_list

    def strMatchFilter(self, orig_list, sdk_list):
        """
        从原列表中过滤 使得不包含指定字符串(sdk_list)
        :param orig_list:
        :param sdk_list:
        :return:
        """
        if orig_list is None or orig_list == [] or sdk_list is None or sdk_list == []:
            return orig_list

        tmp_orig_list = orig_list[:]
        for i in orig_list:
            # 判断不在sdk的字段中
            if i in sdk_list:
                tmp_orig_list.remove(i)
        return tmp_orig_list

    def strContainFilter(self, orig_file_list, white_str_list):
        """
        从原文件列表中过滤 使得不包含相关的白名单字段
        :param orig_list:
        :param file_list:
        :return:
        """
        if orig_file_list is None or orig_file_list == [] or white_str_list is None or white_str_list == []:
            return orig_file_list

        tmp_orig_file_list = orig_file_list[:]      # deep copy
        for file_path in orig_file_list:
            for white_str in white_str_list:
                if white_str in file_path:
                    tmp_orig_file_list.remove(file_path)
                    break
        return tmp_orig_file_list

    def seprateHandMfromFiles(self,allfile_list):
        """
        分离h文件和m文件
        :param allfile_list:
        :return:
        """
        hlist = []
        mmlist = []
        for i in allfile_list:
            if i.endswith(".h"):
                hlist.append(i)
            else:
                mmlist.append(i)
        return hlist, mmlist

    def classdumpContextFromFiles(self, file_path):
        """
        使用classdump获取头文件信息
        :param file_path:
        :return:
        """
        # verify file path
        if not os.path.isfile(file_path):
            print("It is not a vaild File(Mach-O)")
            return None
        # verify mach-o
        macho_type = "CAFEBABE"
        numOfBytes = len(macho_type) / 2
        binfile = open(file_path, "rb") # 二进制
        binfile.seek(0)
        hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes))
        f_hcode = self.bytes2hex(hbytes)
        if f_hcode != macho_type:
            print("It is not a Vaild File(Mach-O)")
            return None

        try:
            class_dump_path = "%s/%s" % (os.path.dirname(os.path.realpath(__file__)), "../utils/class-dump")
            cmd_result = commands.getoutput("%s %s" %( class_dump_path, file_path))
            if cmd_result:
                return cmd_result
        except Exception, e:
            print(e)
            return None





class RegexFilter:

    def __init__(self):
        pass

    def getClsNameFromHeaderList(self, h_path_list):
        """
        从列表中获取类名
        :param h_path_list:
        :return:
        """
        cls_list = []
        for h_header in h_path_list:
            cls_list.extend(self.getClsNameFromFilePath(h_header))
        return cls_list

    def getFuncNameFromMMList(self, mm_path_list):
        """
        从列表中获取函数名
        :param mm_path_list:
        :return:
        """
        func_list = []
        for mm_header in mm_path_list:
            func_list.extend(self.getFuncNameFromFilePath(mm_header))
        return func_list

    def getClsAndFuncFromContext(self,context_str):
        """
        从文本中获取类名方法名
        :param context_str:
        :return:
        """
        if not context_str or context_str.strip() == '':
            return None

        cls_name = re.findall(r'@interface\ (\w+)', context_str)
        result = re.findall(r'(?:^|\n)([\-|\+].*)', context_str)
        flist = []
        for i in result:
            func_name = re.findall(r'\w+', i)[1]
            flist.append(func_name)
        return cls_name + flist

    def getClsAndFuncFromFilePath(self, file_path):
        """
        获取类名和方法名
        :param file_path:
        :return:
        """
        return self.getClsNameFromFilePath(file_path) + self.getFuncNameFromFilePath(file_path)

    def getClsNameFromFilePath(self, file_path):
        """
        从文件中获取类名  b
        :param file_path: 文件的绝对路径 一般是.h
        :return: 一个列表，包含多个类名
        """
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
