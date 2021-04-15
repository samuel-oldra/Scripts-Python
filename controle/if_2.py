a = 'valor' # True
a = 0       # False
a = -1      # True
a = -0.0001 # True
a = ''      # False
a = ' '     # True
a = []      # False
a = {}      # False

if a:
    print('Existe!!!')
else:
    print('não existe ou zero ou vazio...')