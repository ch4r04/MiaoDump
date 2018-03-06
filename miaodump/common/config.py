#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 17:21
# @Author  : ch4r0n
# @Site    : 
# @File    : config.py
# @Software: PyCharm

HEADER_BANNER = '''
                       _      __                     _
  ___   ___       ___ | |__  / _|_   _ ___  ___ __ _| |_ ___  _ __
 / _ \ / __|____ / _ \| '_ \| |_| | | / __|/ __/ _` | __/ _ \| '__|
| (_) | (_|_____| (_) | |_) |  _| |_| \__ \ (_| (_| | || (_) | |
 \___/ \___|     \___/|_.__/|_|  \__,_|___/\___\__,_|\__\___/|_|

                                                    by ch4r0n
[1] Make sure reskey.txt is under the current directory.
[2] Input your project name.
[3] Input salt value, Only letters are allowed.
[4] If successful, an encrypted key-value is output, good luck..

-----------------------------------------------------------------
'''
#系统白名单 需要从文件读取
WHITE_LIST = []
#定义第三方SDK列表
SDK_LIST = ["XGPush","XGSetting","UMSocial","ShareSDK","MJRefresh","Masonry","AFNet","MJExtension","HUPhotoBrowser","MBProgressHUD","FMDB","WMPageController","BlocksKit","LPPopup","Pods","SDWebImage","BaiduMap","CocoaSecurity"]
#定义系统的主要函数列表 必须填.m
SYSTEM_LIST = ['main.m','Main.storyboard','LaunchScreen.xib','LaunchScreen.storyboard']
FILE_NAME = ['main','Main','LaunchScreen']
RES_KEY_PATH = 'reskeys.txt'
#需要加的前缀盐 (字母)
