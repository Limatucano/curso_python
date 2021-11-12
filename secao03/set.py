"""
Set é basicamente um dict sem o key, apenas com value
não aceita elementos repetidos
"""
numeros = {1,2,3,4,5,6,7,8,9,10}

numeros.update([11])
#print(numeros)

#lista com numeros repetidos, pode ser usado o set para retirar numeros repetidos
# numbers = [1,1,2,3,4,2,3,4,5,6,7,8,9]
# print(numbers)
# numbers = set(numbers)
# print(numbers)
# numbers = list(numbers)
# print(numbers)

a1 = {1,2,3,4}
a2 = {3,4,5,6}

a3 = a1.union(a2) #une os dois sets
a4 = a1.intersection(a2) # todos elementos presentes nos dois sets
a5 = a1.difference(a2) # elementos apenas no set da esquerda
a6 = a1.symmetric_difference(a2) # elementos que estão nos dois sets, mas não em ambos
#print(a6)

"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def get_duplicated_number(list_number : list):
    list_aux = []
    for number in list_number:
        if(number in list_aux):
            return number
        list_aux.append(number)
    if len(list_aux) == len(list_number):
        return -1


for list_number in lista_de_listas_de_inteiros: 
    verification = get_duplicated_number(list_number)
    print(verification)

