# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:36:02 2021

@author: Camila Pc

Las columnas en camion.csv corresponden a un nombre de fruta, 
una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. 
Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, 
y calcule el precio pagado por los cajones cargados en el camión.

"""

#costo_camion

with open('../Data/camion.csv', 'rt') as f:
  headers = next(f).split(',')
  costo_total = 0
  for line in f: 
    row = line.split(',')
    fruta = str(row[0])
    cajones = int( row[1])
    precio = float(row[2])
    costo_total += (precio * cajones)
print(costo_total)
         