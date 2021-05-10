nome = 'Samuel-Oldra'

print(nome[0])
# nome[0] = 'T'
print('marca d\'água')  # escape
print('marca d\'água' == "marca d'água")

doc = """
Teste de multiplas linhas
Segunda linha
"""
print(doc)
doc2 = '''
Teste de multiplas linhas
Segunda linha
'''
print(doc2)
print("Texto com multiplas\n\t...linhas")


print(nome[0])
print(nome[5])
print(nome[-4])

print(nome[:6])
print(nome[:-6])
print(nome[7:])
print(nome[-5:])
print(nome[2:5])
print(nome[::])
print(nome[::2])
print(nome[1::2])
print(nome[::-1])
print(nome[::-2])
print()


frase = 'Python é uma linguagem excelente'
print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())
print(frase.split())
print(frase.split('a'))
print()


# Magic Methods
a = '123'
b = ' de oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))
print(len(a))
print(a.__len__())
print('1' in a)
print(a.__contains__('1'))
