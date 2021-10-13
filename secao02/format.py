"""
Formatando valores 
:s - String
:d - Int
:f - float
:.(numero)f - quantidade de casas decimais
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - left
< - right
^ - top

"""

num_1 = 10
num_2 = 3

numero = 10
div = num_1 / num_2

print(f'{div:.2f}')
print(f'{numero:0>4d}')