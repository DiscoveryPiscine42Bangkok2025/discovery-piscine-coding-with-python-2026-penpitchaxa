#!/usr/bin/env python3

x=int(input("Give me the first number: "))
y=int(input("Give me the second number: "))
print("Thank you!")
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} / {y} = {int(x/y) if y != 0 else "second number cannot be 0"}")
print(f"{x} * {y} = {x*y}")
