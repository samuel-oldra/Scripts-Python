y = -1
qtd = 0
total = 0

while(y != 0):
    fatorial = 1

    y = int(input('Digite Y: '))

    if y > 0:
        for n in range(y, 0, -1):
            print(n, end=' ')
            fatorial *= n

        print(f' => {fatorial}')
        total += fatorial
        qtd += 1

print(f'Média dos resultados: {total / qtd}')
