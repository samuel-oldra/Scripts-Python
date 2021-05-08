ex2 = '''
2) Faça um algoritmo que lê valores para uma matriz M[100][4]. Inserir, a
seguir, o menor valor de cada coluna, num vetor VC[4]. No final, mostrar os
valores contidos no vetor.
'''

val_linha = 3  # 100
val_coluna = 4 # 4
matriz = []
vc = []

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

for y in range(0, val_coluna):
    menor_valor = 0
    for x in range(0, val_linha):
        if x == 0 or matriz[x][y] < menor_valor:
            menor_valor = matriz[x][y]
    vc.append(menor_valor)

print()
for z in range(0, val_coluna):
    print(vc[z], end=' ')
