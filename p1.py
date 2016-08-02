#! /usr/bin/python
#coding=utf-8

def mystr(aa,bb,*cc):
	print aa
	print bb
	print cc
mystr(11,2,3,45,55,66)

def fun2(aa,bb,**cc):
	print aa
	print bb
	print cc
fun2(aa=11,bb=223,name='wujun',age=29,sex='woman')
