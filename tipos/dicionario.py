
aluno = {
    'nome': 'Pedro Henrique',
    'nota': 9.2,
    'ativo': True
}

print(type(aluno))
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
print(len(aluno))
print()



pessoa = {
    'nome': 'Prof(a). Ana',
    'idade': 38,
    'cursos': ['Inglês', 'Português']
}
print(type(pessoa))
print(dir(dict))
print(len(pessoa))
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
# print(pessoa['tags'])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))
print()



pessoa = {
    'nome': 'Prof. Alberto',
    'idade': 43,
    'cursos': ['React', 'Python']
}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)
print(pessoa.pop('idade'))
print(pessoa)
pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
