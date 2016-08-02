#!/usr/bin/python
#coding=utf-8
from time import ctime,sleep

def timefun_arg(pre="hello"):
	def timefun(func):
		def wrappedfunc():
			print "%s called at%s %s"%(func.__name__,ctime(),pre)
			print func()
		return wrappedfunc
	return timefun

@timefun_arg("itcast")
def foo():
	pass

@timefun_arg("zjcv")
def too():
	pass

foo()
sleep(2)
foo()

too()
sleep(2)
too()
