#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 15:34
# @Author  : ch4r0n
# @Site    : 
# @File    : encryptor.py
# @Software: PyCharm

import hashlib
from ..common import config

class Encryptor:

    def __init__(self):
        pass

    def secKeyCreate(self, all_keylist):
        '''
        生成安全密钥
        :param all_keylist:
        :return:
        '''
        sec_dic = {}
        for k in all_keylist:
            tempv = hashlib.md5()
            orxst = ""
            for i in range(0, len(k)):
                rst = ord(k[i]) ^ ord(config.SALT_KEY)
                orxst = orxst + chr(rst)
            tempv.update(orxst)
            v = tempv.hexdigest()
            v = '%s%s' %(config.SALT_KEY, v)
            sec_dic[k] = v
        return sec_dic










