#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-10 14:08:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from sys import argv

script,input_file = argv

def print_all(f):  #读文件
	print f.read()

def rewind(f):    #倒回到第一位
	f.seek(0)

def print_a_line(line_count,f):   #一行一行读取
	print line_count,f.readline()

current_file = open(input_file)

print "Firnt let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)

