#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-10 12:50:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
#复制文件
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)#查看文件是不是存在
print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done"

out_file.close()
in_file.close()
