nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (s/n): ') == 's' else False

if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado')

print(nota)
