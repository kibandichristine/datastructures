t=[x*100 for x in range(1,6)]
def gen(n):
    ''' generate n , n-2, n-3,.....,0
    a generator holds a current state'''
    for i in range (n,1,-2):
        yield i

for x in enumerate(gen(20)):
    print(x,end=" ")
print()
#optionally specify begging index
for x in enumerate(t,1):
    print(x,end=" ")
print()