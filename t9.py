#!usr/bin/python
#coding=utf-8
def gen():
	for x in xrange(5):
		tmp=yield x
		if tmp=='hello':
			print "world"
		else:
			print "func wujun",str(tmp)

