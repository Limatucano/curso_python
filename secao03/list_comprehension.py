# Exemplo:
# [expr for item in lista]
# Lê-se aplique a expressão expr em cada item da lista
# com condição:
# [expr for item in lista if condição]
# lista = [item**2 for item in range(10)]
if __name__ == '__main__':
    dobro = [item * 2 for item in range(10)]

    tupla= (
        ('chave','valor'),
        ('chave2','valor2')
    )

    teste = [(y,x) for x,y in tupla]

    one_hundred_numbers = list(range(100))

    only_even_numbers = [value for value in one_hundred_numbers if value % 2 == 0]

    only_odd_numbers = [value for value in one_hundred_numbers if value % 2 == 1]

    teste = [value if value % 2 == 0 else "impar" for value in one_hundred_numbers]

    print(teste)

