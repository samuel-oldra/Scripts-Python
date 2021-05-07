
from string import Template

nome, idade, altura = 'Ana', 30, 1.805

# Mais antiga
print('Nome: %s, Idade: %d, Altura: %.2f, %r, %d' % (nome, idade, altura, True, True))

# Mais Nova - Python < 3.6
print('Nome: {0}, Idade: {1}, Altura: {2}'.format(nome, idade, altura))

# Mais Nova - Python >= 3.6
print(f'Nome: {nome}, Idade: {idade}, Altura: {altura}, 7 = {5 + 2}')

s = Template('Nome: $nome, Idade: $idade, Altura: $altura')
print(s.substitute(nome=nome, idade=idade, altura=altura))
