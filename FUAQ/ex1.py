
x = -1

def ehPar(n):
    return n % 2 == 0


def ehImpar(n):
    return n % 2 == 1


while ehImpar(x):
    x = int(input('Digite X: '))

    if ehImpar(x):
        soma = 0
        for n in range(1, x):
            if ehPar(n):
                soma += n
                print(n, end=' ')
        print(f' => {soma}')