# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:09:58 2021

@author: Camila Pc

A partir de lo que hiciste en el Ejercicio 2.3, 
escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv 
el precio de determinada fruta (o verdura) y lo imprima en pantalla.
 Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.

>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.
"""

#Ejercicio 2.7


def buscar_precio(fruta):
    with open('C:/Users/Cami/Desktop/PYTHON_UNSAM/ejercicios_python/Data/precios.csv', 'rt') as f:
        Fruta = True
        for line in f: 
               row = line.split(',')
               if row[0] == fruta:
                  print('El precio de un cajón de', fruta, 'es:', row[1])
                  Fruta = False
        if Fruta:
                 print(f'{fruta} no figura en el listado de precios.')
        
        