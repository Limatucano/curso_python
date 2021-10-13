# Crie um Programa que seja capas de separar todos os itens de um input exe:
# Degite algo: aodh274?!&:"

# Seu programa dese separar cada item deste input e mostrar todos organizando exemplo de saida:
# Letras:aodh
# Números:274
# Caracteres:?!&:"

# Também podes adicionar um número de cada caracteres 
# Encontrado. Isso me ajudou muito a entender listas.

import re

text = "aodh274?!&:"
r_letters = r"[a-zA-Z]+"
letter = re.findall(r_letters, text)

r_numbers = r"[0-9]+"
numbers = re.findall(r_numbers, text)

r_symbols = r"[^a-zA-Z0-9]+"
symbols = re.findall(r_symbols, text)

print(f"Letras: {letter[0]}")
print(f"Números: {numbers[0]}")
print(f"Simbolos: {symbols[0]}")


