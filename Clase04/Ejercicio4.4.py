# -*- coding: utf-8 -*-
"""
Agregale a tu archivo ejercicio4_1 una función maximo()
 que busque el valor máximo de una lista de números positivos.
 sin usar el comando max.
 agregá una función minimo() al archivo.
"""
from decimal import Decimal
w = Decimal('-Infinity')
b = Decimal('infinity')
def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
    return pos
def buscar_n_elemento(lista,e):
    j = 0  #Inicializamos una variable en 0 la cantidad de veces que e se encuentra en la lista
    for t in (lista):   #recorremos la lista
        if t == e:   #si encontramos e
            j +=1  #sumamos un valor a la cantidad de veces que se encuentra e en la lista
    return j
            
def maximo(lista):

    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = w # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    m = b # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m