# -*- coding: utf-8 -*-
"""
@author: Camila Pc
"""

#EJERCICIO 3.9
"""
En el archivo Data/camion.csv, la primera línea tiene los encabezados de las columnas.
 En los códigos anteriores la descartamos.

>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> encabezados = next(filas)
>>> encabezados
['nombre', 'cajones', 'precio']
>>>
Pero, ¿no puede ser útil conocer los encabezados? Es acá donde la función zip() entra en acción.
 Primero tratá de aparear los encabezados con una fila de datos.
 Modificá la función costo_camion() en el archivo costo_camion.py para que se vea así:

# costo_camion.py

def costo_camion(nombre_archivo):
    ...
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        ...
"""
#%%

import csv 

f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados = next(filas)
fila = next(filas)
record = dict(zip(encabezados, fila))


#%%




import csv


def costo_camion(nombre_archivo):
  f = open(nombre_archivo)
  rows = csv.reader(f)
  headers = next(rows)
  costo_total = 0
  for n_row, row in enumerate(rows, start=1): #leo las lineas y las contabilizo
     record = dict(zip(headers, row))
     try:
         
         cajones = int(record['cajones'])
         precio = float(record['precio'])
         costo_total += cajones * precio
     except ValueError:
        print(f'Fila {n_row}: No pude interpretar: {row}')
  
 
  print('costo total:', float(costo_total))
  f.close()
  

#%%


#Ejercicio 2.16
    
import csv

#Ejercicio 2.17      
       
def leer_camion(nombre_archivo):
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
    return camion

def leer_precios(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    diccionario = {}
    for row in rows:
        try:  
            fruta = row[0]
            precio = float(row[1])
            diccionario[fruta] = precio
        except:
            continue
    return diccionario

def buscar_precio(fruta_buscada):
    f = open('..\Data\precios.csv', "rt")
    precio = 0
    for line in f:
        row = line.strip('\n').split(',')
        fruta = row[0]
        precio_fruta = row[-1]
        if fruta == fruta_buscada:
                precio = precio_fruta
    return float(precio)
     
def balance(nombre_archivo_camion, nombre_archivo_precio):
    
    costo_compra = 0
    ganancia = 0
    recaudacion = 0
    with open(nombre_archivo_camion, 'rt') as f:
       rows = csv.reader(f)
       headers = next(rows)
       for n_row, row in enumerate(rows, start=1): #leo las lineas y las contabiliza
             record = dict(zip(headers, row))
             try:
                 producto = record['nombre']
                 cajones_cant = int(record['cajones'])
                 precio = float(record['precio'])
                 costo_compra += cajones_cant * precio
             except:
                 continue

    camion = leer_camion(nombre_archivo_camion)
    for producto in camion:
            nombre = float(buscar_precio(producto["nombre"]))
            cajones = int(producto["cajones"])
            recaudacion += nombre * cajones
    
    ganancia = recaudacion - costo_compra
            
    print('El costo del camion es de', round(costo_compra, 2))
    print('La recaudación es de', round(recaudacion, 2))
    print('La ganancia es de', round(ganancia, 2))
        
    #Ganancia? 
    
    if ganancia > 0:
        print('Hubo ganancia')
    else:
        print('No hubo ganancia')
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  