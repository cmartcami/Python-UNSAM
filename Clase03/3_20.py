# -*- coding: utf-8 -*-
"""
@author: Camila Pc
#Ejercicio 3.20
Usando contadores  escribí una función contar_ejemplares(lista_arboles) que, 
dada una lista como la que generada con leer_parque(), 
devuelva un diccionario en el que las especies 
(recordá, es la columna 'nombre_com' del archivo) sean las claves y 
tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.
"""
import csv
from pprint import pprint
def leer_parque(archivo, parque):
    with open(archivo, 'rt', encoding = 'utf8') as f:
        arboles = []
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            if row[10] == parque:
                record = dict(zip(headers, row))
                arboles.append(record)
        return arboles

lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')
def contar_ejemplares(lista_arboles):
        from collections import Counter
        ejemplares = Counter()
        for s in lista_arboles:
            ejemplares[s['nombre_com']] += 1
        return ejemplares
ejemplares_contador = contar_ejemplares(lista_arboles)
pprint(ejemplares_contador)
pprint(ejemplares_contador.most_common(5))