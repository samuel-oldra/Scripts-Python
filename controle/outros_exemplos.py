pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')

for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2:  # impar
        continue
    print(i)

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('Fim!')
