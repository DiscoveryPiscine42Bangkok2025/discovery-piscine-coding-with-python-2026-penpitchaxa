#!/usr/bin/env python3

import sys

param=len(sys.argv)-1
if(param!=1):
	print("none")
else:
	print(sys.argv[1].upper())
