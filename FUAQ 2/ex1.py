ex1 = '''
1) Faça um algoritmo que lê valores para as variáveis A e B. Consistir para que
B recebe obrigatoriamente um valor maior que A. Calcular e mostrar os fatoriais
dos valores ímpares existentes entre A e B. Os cálculos de fatorial devem ser
realizados dentro de uma função e os resultados mostrados no programa principal.
No final, mostrar a média dos resultados dos fatoriais calculados.
'''

a = b = -1
qtd = soma = 0

def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat


while (a < 0):
    a = int(input('Digite A (> 0): '))

while(b < a):
    b = int(input('Digite B (> A): '))

for i in range(a, b + 1):
    # Ímpares
    if i % 2 != 0:
        fat = fatorial(i)
        qtd += 1
        soma += fat
        print(f'{i}! = {fat}')

print(f'A média dos fatoriais é {soma / qtd}')
