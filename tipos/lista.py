nums = [1, 2, 3]

print(type(nums))

nums.append(3)
nums.append(4)
nums.append(500)

print(len(nums))
print(2 in nums)

nums[3] = 100
nums.insert(0, -200)

print(nums[6])
print(nums[-1])
print(nums[-2])
print(nums)
print()


# Mais sobre listas
nova_lista = [1, 5, 'Ana', 'Bia']

print(nova_lista)

nova_lista.remove(5)

print(nova_lista)

nova_lista.reverse()

print(nova_lista)

nova_lista.append([3, 4])

print(nova_lista)
print(nova_lista.index('Ana'))
print(nova_lista[0])
print(1 in nova_lista)
print('Bia' in nova_lista)
print('Pedro' not in nova_lista)
print(nova_lista[-1])
print()


lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
