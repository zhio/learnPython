# -*- coding: utf-8 -*-
from sys import argv#引用了一个模块
script,filename = argv

txt = open(filename)#打开文件

print "Here's your file %r:" %filename#输出文件名
print txt.read()#打印文件内容

print "Type the filename again:"
file_again = raw_input(">")#再次打开文件

txt_again = open(file_again)#打开文件

print txt_again.read()