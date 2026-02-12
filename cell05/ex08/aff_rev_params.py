#!/usr/bin/env python3

import sys

param=len(sys.argv)-1
if(param<3):
	print("none")
else:
	while(param>0):
		print(sys.argv[param])
		param-=1
