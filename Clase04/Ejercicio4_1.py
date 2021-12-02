# -*- coding: utf-8 -*-
"""
Escribir una función buscar_u_elemento() que reciba una lista
 y un elemento y devuelva la posición de la última aparición 
 de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
 Agregale a tu programa una función buscar_n_elemento() 
 que reciba una lista y un elemento y devuelva la cantidad 
 de veces que aparece el elemento en la lista. 
"""
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
    j = 0
    for t in (lista):
        if t == e:
            j +=1 
    return j
            