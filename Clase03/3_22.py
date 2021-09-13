# -*- coding: utf-8 -*-
"""
@author: Camila Pc
Escribí una función obtener_inclinaciones(lista_arboles, especie) que,
 dada una especie de árbol y una lista de árboles como la anterior, 
 devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie.
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
                    record['altura_tot'] = float(record['altura_tot'])
                    arboles.append(record)
        return arboles

lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')
especie = 'Jacarandá'
def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    especie = especie.upper()   #Mayusculas todo para normalizar
    for r in lista_arboles:
       inclinaciones = 0
       if(r['nombre_com'].upper()==especie or especie=='*'):
           inclinaciones = r['inclinacio']
           inclinacion.append(inclinaciones)
    return inclinacion