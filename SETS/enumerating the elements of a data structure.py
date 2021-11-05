lst=[x for x in range(10,51,10) ]
for i in range (len(lst)):
    print(i,lst[i])


print()
'''
The –builtins—module provides a function named enumerate that returns an iterable 
object that produces tuples. Each tuple pairs with an index with its associated element. 
The following performs the same function:
'''
print('using enumerate')
for i,elem in enumerate(lst):
    print(i,elem)
print()
t=[x*100 for x in range(1,6)]
s={x for x in range(1000,5001,1000)}
d={'A':4,'B':18,'C':0,'D':3}
for x in enumerate(lst):
    print(x,end="")
print()
for x,wam in enumerate(t):
    print(x,wam,end="")
print()
for x in enumerate(d):
    print(x,end="")
print()
for x in enumerate(s):
    print(x,end="")
print()