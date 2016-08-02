#!/usr/python
#coding=utf-8
class student(object):
	'''
	2015 new student
	'''
	grade=2015
	__school="qinghua"
	
	def __init__(self,subj,name,age,sex):
		'''this is create fun'''
		self.subj=subj
		self.name=name
		self.age=age
		self.sex=sex
		print "init student"

	def setName(self,newname):
		self.name=newname

	def getName(self):
		return self.name

	def showstudent(self):
		print "subj=",self.subj
		print "name=",self.name
		print "age=",self.age
		print "sex=",self.sex
		print "grade=",student.grade
		print "school=",student.__school
	@classmethod
	def updategrade(cls,newgrade):
		cls.grade=newgrade

	@classmethod
	def showclass(cls):
		print "__name__=",cls.__name__
		print "__dict__=",cls.__dict__
		print "__clasd__=",cls.__class__
