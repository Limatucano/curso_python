hora = input("digite a hora:")
minuto = input("digite o minuto:")
tempo = f"{hora}:{minuto}"
if(int(hora) in range(0,11)):
    print(f"Bom dia grupo, hora: {tempo}")
elif(int(hora) in range(12,17)):
    print(f"Boa tarde familia, hora: {tempo}")
elif(int(hora) in range(18,23)):
    print(f"buenas noites, hora: {tempo}")