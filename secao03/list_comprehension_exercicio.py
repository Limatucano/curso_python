string = '01234567890123456789012345678901234567890123456789'
#deve ficar assim: ['0123456789','0123456789','0123456789','0123456789','0123456789']
#para depois ficar assim '0123456789.0123456789.0123456789.0123456789.0123456789'
SIZE = 10
lista = [string[start:start + SIZE] for start in range(0, len(string), SIZE)]

string = '.'.join(lista)
print(string)