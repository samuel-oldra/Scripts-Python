ex3 = '''
3) Faça um algoritmo que lê valores para uma matriz W[5][6]. A seguir, inserir,
de forma compactada, num vetor U[30] os valores pares contidos na matriz que
possuírem fatorial maior que 1000 (hum mil).
'''

val_linha = 3  # 5
val_coluna = 4 # 6
matriz = []
vetor_u = []

def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat


for x in range(0, val_linha):
    colunas = []
    for y in range(0, val_coluna):
        valor = int(input(f'Digite o valor para a célula [{x + 1}, {y + 1}]: '))
        colunas.append(valor)
    matriz.append(colunas)

# Imprimir matriz
for x in range(0, val_linha):
    for y in range(0, val_coluna):
        print(matriz[x][y], end=' ')
    print()

print()
for x in range(0, val_linha):
    for y in range(0, val_coluna):
        fat = fatorial(matriz[x][y])
        if matriz[x][y] % 2 == 0 and fat > 1000:
            # vetor_u.append(f'{matriz[x][y]}! = {fat}')
            vetor_u.append(matriz[x][y])

print('Vetor U:', end=' ')
for z in range(0, len(vetor_u)):
    print(vetor_u[z], end=' ')
