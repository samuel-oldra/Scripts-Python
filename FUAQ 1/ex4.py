qtd = 0
inicial = 100


def ehPerfeito(n):
    soma = 0

    for val in range(1, n):
        if n % val == 0:
            soma += val

    if soma == n:
        return True
    else:
        return False


while qtd < 4:
    inicial += 1

    if(ehPerfeito(inicial)):
        qtd += 1
        print(inicial, end=' ')
