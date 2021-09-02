# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:12:49 2021

@author: Camila Pc

Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus 
traducciones al geringoso (como en el Ejercicio 1.18). 
Probá tu función para la lista ['banana', 'manzana', 'mandarina'].
"""

def diccionario_geringoso(lista_palabras):
    palabras = lista_palabras
    vocal = ['a','e','i','o','u','A','E','I','O','U']
    cadena_geringosa = ''
    d = {}
    for index in range(len(lista_palabras)): 
      elementos = palabras[index]
      for c in elementos: 
        if c in vocal:
          c = c + 'p' + c
          cadena_geringosa += c
        else:
          c = c
          cadena_geringosa += c
      d[lista_palabras[index]] = cadena_geringosa
      cadena_geringosa = ''
    print(d)
    
