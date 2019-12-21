import numpy as n
a=n.array(input('enter the array'))
b=n.array(input('enter the array2'))
for i in b:
	if(i>0):
		a = n.append(a,i)
print a
