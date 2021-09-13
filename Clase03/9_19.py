# -*- coding: utf-8 -*-
"""
@author: Camila Pc
"""
#Ejercicio 3.19

"""
Escribí una función especies(lista_arboles) que tome una lista de árboles como 
la generada en el ejercicio anterior y devuelva el conjunto de especies
 (la columna 'nombre_com' del archivo) que figuran en la lista.
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
def especies(lista_arboles):
      especies = set()
      for i in lista_arboles:
          especies.add(i['nombre_com'])
      return especies
  
nombre_especie = especies(lista_arboles)