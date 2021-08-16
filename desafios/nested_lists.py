if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
    
    lista.sort(key=lambda x:x[1])
    print(lista[0][0])
    print(lista[1][0])