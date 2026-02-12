#!/usr/bin/env python3

import sys

param=len(sys.argv)-1
if(param!=2):
	print("none")
else:
	count=0
	arr=sys.argv[2].split(" ")
	for i in arr:
		if(i==sys.argv[1]):
			count+=1
	if(count==0):
		print("none")
	else:
		print(count)
