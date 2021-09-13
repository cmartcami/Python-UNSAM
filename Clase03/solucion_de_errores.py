# -*- coding: utf-8 -*-
"""
En los siguientes ejercicios te proponemos que uses las técnicas que mencionamos 
arriba para resolver los problemas que aparecen a continuación. 
Determiná los errores de los siguientes códigos y corregilos en un archivo 
solucion_de_errores.py comentando brevemente los errores. 
@author: Camila Pc
"""
"""
#Ejercicio 3.1

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#Comentario: El error era que solo tomaba las palabras que empezaban con'a' y no las que las contenian.
#A continuacion el codigo corregido
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%

# Ejercicio 3.2
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Acá entiendo que el error es que no toma la 'A' de UNSAM. Además habia un error de sintaxis, faltaban algunos ':' y decía falso en vez de false
"""
#Corregido -->

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    letras = ['a', 'A']
    while i<n:
        if expresion[i] in letras:
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%

#Ejercicio 3.3
"""
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

"""
#EL error está en que 1984 no admite len, podría ponerse a 1984 como string.

#%%

#Ejercicio 3.4
"""
def suma(a,b):
    c = a + b


a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} =", c)

#El error está en que función no devuelve nada
#corrección ---->
"""
def suma(a,b):
    c = a + b
    return c



a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} =", c)

#%%

#Ejercicio 3.5
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

"""
#Entiendo que el error está en que se sobreescribe
#Solucion -->


import csv
from pprint import pprint

def leer_camion(nombre_archivo):

    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
        return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#Entendí que debia reiniciar el diccionario en cada iteración, no termino de entender por que primero me imprime naranja 7 veces y despues el resto





























