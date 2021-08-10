from datetime import date 

ano = date.today().year
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
ano_nascimento = int(ano) - idade
imc = peso/(altura*altura)

print(f'nome:{nome}, idade:{idade}, altura:{altura}, peso:{peso}, ano de nascimento:{ano_nascimento}, imc:{imc}')