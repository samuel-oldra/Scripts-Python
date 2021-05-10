nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

x = ('Bia')
print(type(x))
y = ('Bia',)
print(type(y))

print('Bia' in nomes)

print(nomes[0])
print(nomes[1:3])
print(nomes[1:-1])
print(nomes[2:])
print(nomes[:-2])

print(len(nomes))
print(type(nomes))
print(nomes)
print()


tupla = tuple()
print(type(tupla))
tupla = ()
print(type(tupla))
# print(dir(tuple))
# help(tuple)

tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))
print(tupla[0])
# tupla[0] = 'novo'

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))
