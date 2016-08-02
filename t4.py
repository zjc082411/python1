#!usr/bin/python

import os
ls=os.linesep

while True:
	if os.path.exists(fname):
		print "ERROR: '%s' already exists" % fname
	else:
		break
all=[]
print "\nEnter lines('.' by itself to quit).\n"
