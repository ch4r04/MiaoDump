#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 19:33
# @Author  : ch4r0n
# @Site    : 
# @File    : miaodump_client.py
# @Software: PyCharm

import argparse

def main():
    opts = argparse.ArgumentParser(description="miaodump client")
    opts.add_argument('-p', '--path', default=None,
                      help="Dir to using the miaodump")
    opts.add_argument('-e', '--exclude', help="Exclude the SDK from file")
    opts.add_argument('-ed', '--exclude-default', help="using default value to filter the file")
    opts.add_argument('-a', '--arch',help="arch from binary file")
    opts.add_argument('-o', '--output', help="output the header files")

    args = opts.parse_args()





