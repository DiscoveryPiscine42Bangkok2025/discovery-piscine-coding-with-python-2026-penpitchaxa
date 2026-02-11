#!/usr/bin/env python3

inp=int(input("Enter a number less than 25\n"))
if inp>=25:
	print("Error")
else:
	while(inp<=25):
		print(f"Inside the loop, my variable is {inp}")
		inp+=1

