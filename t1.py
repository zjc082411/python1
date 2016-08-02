#!/usr/bin/python
#coding=utf-8
def fun1(aa,bb,*c):
	print aa
	print bb
	print c

fun1(11,22,33,'aa','bb',23,'tt')

def fun2(aa,bb,**c):
	print aa
	print bb
	print c

fun2(11,22,name='jian',age=30)
