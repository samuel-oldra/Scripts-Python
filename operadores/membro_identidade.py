
# Operador de Membro

lista = [1, 2, 3, 'Ana', 'Clara']
print(2 in lista)
print('Ana' not in lista)
print()

# Operador de Identidade

x = 3
y = x
z = 3
# Comparação de valores
print(x is y)
print(y is z)
print(x is not z)
print()

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
# Comparação de referências
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)
