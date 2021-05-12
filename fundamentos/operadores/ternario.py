lockdown = True
grana = 30

status = 'Em casa' if lockdown or grana >= 100 else 'Uhuuu'

print(f'O status é: {status}')


esta_chovendo = True
print('Estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('Estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))
