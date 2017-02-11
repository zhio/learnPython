#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-09 19:03:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from sys import argv

script,filename = argv

print "We're going to erase %r." % filename
print "opening the file ..."
target = open(filename,'w')
#print target.read()

print "Truncating the file. Goodbye"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."
target.close()
file_again = raw_input(">")#再次打开文件

txt_again = open(file_again)#打开文件

print txt_again.read()
#target.open(filename)
#print target.read()#为什么不能这么写？