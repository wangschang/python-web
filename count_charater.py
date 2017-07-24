
#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#统计输入文件的字母出现字数

import pprint
import collections


def main():

    file_input =  raw_input('File Name: ')
    with open(file_input, 'r') as info:
        count = collections.Counter(info.read().upper())

    value = pprint.pformat(count)
    print(value)


if __name__ == "__main__":
    main()
