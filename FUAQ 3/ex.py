ex = '''Um algoritmo (em Python) que, inicialmente, lê valor para um vetor com
20 elementos. Após completar a leitura do vetor, o algoritmo deve ler um valor
para uma variável de nome ‘chave’ (que não é vetor e guarda apenas um valor por
vez) e, na sequência, realizar numa função recursiva uma busca binária do valor
digitado para a variável ‘chave’. A função deve retornar para o programa
principal o índice do elemento do vetor onde o valor digitado foi encontrado
(na hipótese de o valor realmente estar dentro do vetor) ou um valor de exceção
(ex: um valor negativo) para informar que o valor não está dentro do vetor (na
hipótese do valor não estar dentro do vetor). O programa principal deve então,
ou mostrar o índice onde o valor de ‘chave’ foi encontrado ou informar que o
valor de ‘chave’ não está no vetor.'''


def busca_binaria_recursiva(vetor, chave, esquerda, direita):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    if vetor[meio] == chave:
        return meio
    elif vetor[meio] > chave:
        return busca_binaria_recursiva(vetor, chave, esquerda, meio - 1)
    else:
        return busca_binaria_recursiva(vetor, chave, meio + 1, direita)


qtd_itens = 5  # 20 itens para o vetor
vetor = []

for i in range(0, qtd_itens):
    valor = input(f'Digite o valor da posição {i + 1}: ')
    vetor.append(valor)

chave = input('Digite o valor da "chave": ')

print('Chave                  : ' + chave)
print('Vetor                  : ' + str(vetor))
print('Índice Busca Padrão    : ' + str(vetor.index(chave)))

vetor.sort()
indice = busca_binaria_recursiva(vetor, chave, 0, len(vetor))
print('Vetor Ordenado         : ' + str(vetor))
print('Índice Busca Bin. Rec. : ' + str(indice))
