#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
import os  
import sys  
import shutil  
  
# call the delete_svn function  
def delete_svn(root_dir):  
    subdir_list = os.listdir(root_dir)  
    for name in subdir_list:  
        to_delete_name = os.path.join(root_dir, name)  
        if name == '.svn':  
            shutil.rmtree(to_delete_name, ignore_errors=None)  
            print 'deleting the ' + to_delete_name  
            continue  
        if os.path.isdir(to_delete_name):  
            delete_svn(to_delete_name)  
  
# check the length of params  
if len(sys.argv) < 2:  
    print 'Please specify the dir path'  
    sys.exit()  
  
# check if the input dir path is valid  
root_dir = sys.argv[1]  
if not os.path.exists(root_dir):  
    print 'Pleanse specify an existing path'  
    sys.exit()  
  
# check if the input dir path is a directory  
if not os.path.isdir(root_dir):  
    print 'Please specify an directory path'  
    sys.exit()  
  
delete_svn(root_dir) 
