'''
 uso de args e kwargs
 args = tupla
 kwargs = dict

'''



def teste(*args, **kwargs):
    sobrenome = kwargs.get('sobrenome')

    if sobrenome:
        print(sobrenome)
        return
    print("não tem sobrenome")

lista = [1,2,3,4,5,6,7,8,9]

teste(*lista, nome="Matheus")