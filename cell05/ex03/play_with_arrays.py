#!/usr/bin/env python3

orig=[2,8,9,48,8,22,-12,2]
new=set()
for i in orig:
	if(i>5):
		new.add(i+2)
print(orig)
print(new)
