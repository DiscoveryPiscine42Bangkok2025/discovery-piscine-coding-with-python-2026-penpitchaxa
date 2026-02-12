#!/usr/bin/env python3

import sys

param=len(sys.argv)-1
if(param==0):
	print("none")
else:
	print(f"parameter: {param}")
	for i in range(1, param+1):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
