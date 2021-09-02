# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:03:49 2021

@author: Camila Pc
"""




import csv

def leer_camion(nombre_archivo):
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
    return camion

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

camion = costo_camion('../Data/camion.csv')
print(camion)
