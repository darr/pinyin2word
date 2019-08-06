#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-06 21:53
# Modified date : 2019-08-06 21:54
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from pinyin2chinese import *

transer = PinyinWordTrans()
while(1):
    pinyin_list = input('enter an sent to transfer:')
    result = transer.trans(pinyin_list)
    print(result)
