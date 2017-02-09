#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-09 16:58:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said :'%s'" % y

hilarious = False
joke_ebaluation = "Isn't that joke so funny?! %r"

print joke_ebaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side"

print w + e