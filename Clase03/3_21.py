# -*- coding: utf-8 -*-
"""
@author: Camila Pc


Escribí una función obtener_alturas(lista_arboles, especie) que,
 dada una lista de árboles como la anterior y una especie de árbol 
 (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas 
 (columna 'altura_tot') de los ejemplares de esa especie en la lista.
"""

import statistics
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
def obeter_alturas(lista_arboles, especie):
    alturas = []
    especie = especie.upper()   #a Mayusculas todo para normalizar
    for r in lista_arboles:
       altura = 0
       if(r['nombre_com'].upper()==especie or especie=='*'):
           altura = r['altura_tot']
           alturas.append(altura)
    promedio = statistics.mean(alturas) #Calcula el promedio de la lista
    altura_maxima = max(alturas)
    print(f'La altura máxima de {especie} es de {altura_maxima} m. y el promedio de alturas de esa especie es de {promedio} m.')
