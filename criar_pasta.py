import os
l = int(input('digite a quantidade de pastas que deseja:'))

for x in range(1, l + 1):
    os.mkdir(f'./secao{str(x).zfill(2)}')