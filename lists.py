'''
this is an object that hold a collection of objects, it represents a sequence of data .
it need not to be homogeneous.
a list variable can be local or global,and it must be defined before
'''
import math as mt
lst=list((-3,54,-5,5,56,9))
print(type(lst))
lst[2]=7
print(lst)
print(lst[-1])
lst[1],lst[3],lst[-1]=mt.sqrt(81),mt.sqrt(64)+2,8
print(lst)
