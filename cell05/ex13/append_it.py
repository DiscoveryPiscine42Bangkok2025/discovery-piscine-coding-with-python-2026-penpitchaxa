#!/usr/bin/env python3

import sys

def main():
	param=len(sys.argv)-1
	if(param==0):
		print("none")
		return
	for i in range (1,param+1):
		if("ism" not in sys.argv[i]):
			print(sys.argv[i]+"ism")
main()
