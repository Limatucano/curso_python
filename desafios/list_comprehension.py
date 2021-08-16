# Exemplo:
# [expr for item in lista]
# Lê-se aplique a expressão expr em cada item da lista
# com condição:
# [expr for item in lista if condição]
# lista = [item**2 for item in range(10)]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    teste = []
    lista = [[one,two,tree] for one in range(x + 1) for two in range(y+1) for tree in range(z+1) if(one+two+tree != n)]
    print(lista)
