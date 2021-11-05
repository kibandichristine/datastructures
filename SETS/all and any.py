s={x**2 for x in range (10)}
print(s)
u=[x>0 for x in s]
print(u)


print()
t={8,4,6,3,5,6,8}
print(all([x>0 for x in t ]))

print()
print(all((x>0 for x in t)))
