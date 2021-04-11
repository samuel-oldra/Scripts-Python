# x = 10
#
# while x:
#     print(x)
#     x -= 1
#
# print('Fim!')

nota = 0
qtde = 0
total = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

if qtde:  # Evitar divisão por zero
    print(f'A média da turma é {total / qtde}')
