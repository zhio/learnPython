#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-09 18:20:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from sys import argv

script, user_name = argv
prompt = '> '#用户输入提示符

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
#一个交互式游戏的雏形