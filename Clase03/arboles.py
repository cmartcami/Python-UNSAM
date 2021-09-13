# -*- coding: utf-8 -*-
"""
@author: Camila Pc

leer_parque('../Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')
Definí una función leer_parque(nombre_archivo, parque) 
que abra el archivo indicado y devuelva una lista de diccionarios 
con la información del parque especificado. La lista debe tener un 
diccionario por cada árbol del parque elegido. Dicho diccionario debe
 tener los datos correspondientes a un árbol (recordá que cada fila del
                                              csv corresponde a un árbol).

"""

#3.18

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



