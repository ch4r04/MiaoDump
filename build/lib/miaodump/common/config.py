#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:21
# @Author  : ch4r0n
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import datetime
import os

HEADER_NAME = "miaodump_header.h"

HEADER_BANNER = '''
// __  __ _             ____
//|  \/  (_) __ _  ___ |  _ \ _   _ _ __ ___  _ __
//| |\/| | |/ _` |/ _ \| | | | | | | '_ ` _ \| '_ \\
//| |  | | | (_| | (_) | |_| | |_| | | | | | | |_) |
//|_|  |_|_|\__,_|\___/|____/ \__,_|_| |_| |_| .__/
//                                           |_|
//
//                                                    by ch4r0n
//[1] This script is just for exporting header files(encrypted).
//[2] Security is not now, and will never be based purely on Obscurity.
//[3] You can delete if you don't need the defines.
//[4] There may be some bugs, good luck.
//                                            %s
//-----------------------------------------------------------------
#ifndef MIAODUMP_Header
#define MIAODUMP_Header
''' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

HEADER_TAIL = '''
#endif
'''

#系统白名单 需要从文件读取
WHITE_LIST = []
#定义第三方SDK列表
SDK_LIST = ["Pod","XGPush","XGSetting","UMSocial","ShareSDK","MJRefresh","Masonry","AFNet","MJExtension","HUPhotoBrowser","MBProgressHUD","FMDB","WMPageController","BlocksKit","LPPopup","Pods","SDWebImage","BaiduMap","CocoaSecurity"]
RES_KEY_PATH = "%s/%s"% (os.path.dirname(os.path.realpath(__file__)), '../utils/reskeys.txt')

#需要加的前缀盐 (字母)
SALT_KEY = 'A'


