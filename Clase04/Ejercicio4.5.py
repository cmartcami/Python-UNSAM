# -*- coding: utf-8 -*-
"""
Escribí una función invertir_lista(lista) que dada una lista devuelva
 otra que tenga los mismos elementos pero en el orden inverso.
 Es decir, el que era el primer elemento de la lista de entrada deberá 
 ser el último de la lista de salida y análogamente con los demás elementos.
"""


def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.append(e)
    invertida.sort(reverse=True)
    return invertida
