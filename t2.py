#!/usr/bin/python
#coding=utf-8
def counter(start=0):
	count=[start]
	def incr():
		count[0]+=1
		return count[0]
	return incr

