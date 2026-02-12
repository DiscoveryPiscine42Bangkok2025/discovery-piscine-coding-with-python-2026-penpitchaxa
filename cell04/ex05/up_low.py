#!/usr/bin/env python3

inp=input()
for i in inp:
	if(i.isalpha()):
		if(i.isupper()):
			print(i.lower(),end="")
		else:
			print(i.upper(),end="")
	else:
		print(i,end="")
print()
