# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:16:14 2021

@author: Camila Pc

El archivo ../Data/precios.csv contiene una serie de líneas con precios de venta de 
cajones en el mercado al que va el camión. El archivo se ve así:

"Lima",40.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",53.72
...

Escribí un código que abra el archivo ../Data/precios.csv, 
busque el precio de la naranja y lo imprima en pantalla.

"""

with open('../Data/precios.csv', 'rt') as f:
    headers = next(f).split(',')
    costo_total = 0
    for line in f:
        row = line.split(',')
        if row[0] == 'Naranja':
            print('El precio de la naranja es igual a', row[1])   