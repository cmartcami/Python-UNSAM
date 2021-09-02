"""
Geringoso rústico
Usá una iteración sobre el string cadena para agregar la sílaba 
'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
"""

vocal = ['a','e','i','o','u','A','E','I','O','U']

cadena = input('Ingrese palabra:')
capadepenapa = ''

for c in cadena:
     if c in vocal:
        c = c + 'p' + c
        capadepenapa = capadepenapa + c
     else:
        c = c
        capadepenapa = capadepenapa + c
        
print(capadepenapa)