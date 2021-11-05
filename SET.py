'''
union: A | B - elements in A & B or both  -  set
intersection: A & B -  elements common to both  -  set
set difference: A-B   -elements in A but not B  -  set
symmetric difference: A^B    -elements in A or B but not both   -set
set membership : x not in/(in)A   -x isn't a member of A/     -bool
                                    X is a member of A
set equality : A==B     - set A and B contains exactly the same  elements    -bool
subset: A<=B        -every element in set A is also a member of set b   -bool
proper subset :A<B    -A is a subset B, but B contains at least one elements not in A
'''
s={2,5,665,46,5,8,3,1,3}
t={8,4,6,3,5,6,8}
u = {2,5,665,46}
print('union',s|t)
print('intersection',s&t)
print('set diff',s-t)
print('proper subset: ',u<s)
print(t in s)

print('\nusing list compressions')
s={x**2 for x in range (10)}
print(s)

