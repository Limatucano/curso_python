first_nome = input("digite o seu primeiro nome")

if(len(first_nome) <= 4):
    print("seu nome é curto")
elif(len(first_nome) in range(5,7)):
    print("seu nome é normal")
else:
    print("seu nome é grande")