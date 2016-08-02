#!usr/bin/python
#coding=utf-8
from time import ctime,sleep

def timefun(func):
	def wrappedfunc(a,b):
		print "%s called at %s"%(func.__name__,ctime())
		print a,b
		return func(a,b)
	return wrappedfunc

@timefun
def foo(a,b):
	print a+b

foo(3,5)
sleep(2)
foo(2,4)

def timefun1(func):
	def son():
		print "%s called at%s"%(func.__name__,ctime())
		return func()
	return son

@timefun1
def too():
	print "in too"


too()
sleep(2)
too()
