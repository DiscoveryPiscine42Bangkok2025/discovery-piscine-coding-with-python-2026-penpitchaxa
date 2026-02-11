#!/usr/bin/env python3

num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))

mul=num1*num2
print(f"{num1} x {num2} = {mul}")

if mul>0:
	print("The result is positive.")
elif mul<0:
	print("The result is negative.")
elif mul==0:
	print("The result is positive and negative.")
