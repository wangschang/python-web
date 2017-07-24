#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 统计输入文件的字母出现字数

import pprint
import collections
import os

def main():
    filename =  raw_input('File Name: ')
    if not os.path.isfile(filename):
        print('文件不存在')
        exit()
    with open(filename, 'r') as info:
        count = collections.Counter(info.read().upper())

    value = pprint.pformat(count)
    print(value)


if __name__ == "__main__":
    main()
