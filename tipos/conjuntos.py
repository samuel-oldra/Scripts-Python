print({1, 2, 3})
print(type({1, 2, 3}))

conj = {1, 2, 3, 3, 3, 3, 3, 3}
#print(conj[1]) # Não acessa índices
print(conj)
print(len(conj))
print()



a = {1, 2, 3}
print(type(a))
# a[0]
a = set('coddd3r')
print(a)
print('3' in a, '4' not in a)
print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)

print(c1 >= c2)
print(c2 <= c1)

print({1, 2, 3} - {2})
print(c1 - c2)

print(c1)
c1 -= {2}
print(c1)
