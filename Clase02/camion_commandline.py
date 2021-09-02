# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:38:12 2021

@author: Camila Pc

Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py 
que incorpore la lectura de parámetros por línea de comando según la sugerencia del siguiente ejemplo:

# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
sys.argv es una lista que contiene los argumentos que le pasamos al script al momento 
de llamarlo desde la línea de comandos (si es que le pasamos alguno). 
Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr nuestro programa 
y que procese el mismo archivo podríamos escribir:

bash $ python3 camion_commandline.py ../Data/camion.csv
Costo total: 47671.15
bash $
O con el archivo missing.csv:

bash $ python3 camion_commandline.py ../Data/missing.csv
...
Costo total: 30381.15
bash $
Si no le pasamos ningún archivo, va a mostrar el resultado para camion.csv 
porque lo indicamos con la línea nombre_archivo = '../Data/camion.csv'.


"""

import csv
import sys


def costo_camion(nombre_archivo):
  f = open(nombre_archivo)
  rows = csv.reader(f)
  headers = next(rows)
  headers
  costo_total = 0
  for row in rows: 
     try:
        cajones = int( row[1])
        precio = float(row[2])
        costo_total += (precio * cajones)
     except ValueError:
         print('Cuidado, faltan datos')
  print('costo total:', float(costo_total))
  f.close()


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/Cami/Desktop/PYTHON_UNSAM/ejercicios_python/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo) 