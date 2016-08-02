#!usr/bin/python
#coding=utf-8
class parent:
	parentAttr=100

	def __init__(self):
		print"parent construction"
	def parentMethod(self):
		print "parent method"
	def setAttr(self,attr):
		parent.parentAttr=attr
	def getAttr(self):
		print parent.parent.Attr
class Child(parent):
	def __init__(self):
		parent.__init__(self)
		
	def showchild(self):
		print "child "

