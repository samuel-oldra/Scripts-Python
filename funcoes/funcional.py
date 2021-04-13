
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

somar = soma
print(somar(3, 4))

def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

def soma_parcial(a):
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 10s
    # processamento pesado 3 - 40s
    def concluir_soma(b):
        return a + b # 10s
    return concluir_soma

# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s

soma_1 = soma_parcial(1) # 1m
r1 = soma_1(2) # +10s
r2 = soma_1(3) # +10s
r3 = soma_1(4) # +10s

fn = soma_parcial(10)
resultado = fn(12)
print(resultado)

resultado = soma_parcial(10)(12)
print(resultado, r1, r2, r3)
