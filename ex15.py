#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-10 14:32:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

def add(a,b):
	print " ADDING %d + %d" %(a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTPLYING %d * %d" %(a,b)
	return a * b

def divide(a,b):
	print "DIBIDING %d / %d" %(a,b)
	return a / b

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, height: %d,weight: %d,iq: %d" %(age,height,weight,iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"