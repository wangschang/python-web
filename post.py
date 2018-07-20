#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
调用post
'''
import os,sys
import urllib,urllib2

def main():
    url = 'http://xxxx/msg/HttpBatchSendSM'
    msg = '您的验证码是123456'
    values = {  
            'msg' : msg,
            'mobile':'18518100000'
             }   
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print('%s' % the_page)

if __name__ == '__main__':
    main()
