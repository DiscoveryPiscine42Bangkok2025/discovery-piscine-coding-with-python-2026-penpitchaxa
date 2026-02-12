#!/usr/bin/env python3

import sys
param=len(sys.argv)-1
if(param!=1):
	print("none")
else:
	inp=input("What was the parameter? ")
	if (inp==sys.argv[1]):
		print("Good job!")
	else:
		print("Nope, sorry...")
