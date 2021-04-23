
x = 0
y = 0

def ehPrimo(n):
    for count in range(2, n):
        if (n % count == 0):
            return False
    return True


x = int(input('Informe X: '))

while(x > y):
    y = int(input('Informe Y: '))

for n in range(x + 1, y):
    if (ehPrimo(n)):
        print(n, end=' ')