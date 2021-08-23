try:
    number = int(input("digite um numero"))
    print("par" if number % 2 == 0 else "impar")
except:
    print("aceitamos apenas numero inteiro")
