from functools import reduce

notas = [6.4, 7.2, 5.4, 8.4]

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#    notas[i] = notas[i] + 1.5

def nota_mais_um_e_meio(nota):
    return nota + 1.5

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas_finais_1 = map(nota_mais_um_e_meio, notas)
notas_finais_2 = map(somar_nota(1.6), notas)

print(list(notas_finais_1))
print(list(notas_finais_2))



# total = 0
# for n in notas:
#     total += n
#
# print(total)

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)
