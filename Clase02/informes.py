# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:56:46 2021

@author: Camila Pc

Supongamos que los precios en camion.csv son los precios pagados al productor 
de frutas mientras que los precios en precios.csv son los precios de venta en el 
lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que 
hiciste recién en tu programa informe.py (usando las funciones leer_camion() 
y leer_precios()) y completá el programa para que con los precios del camión 
(Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, 
lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? 
El programa debe imprimir por pantalla un balance con estos datos.
"""

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

       
       
       #Ejercicio 2.18
       
       
       
       
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
       headers = next(f)
       headers
       for row in rows:
             producto = row[0]
             cajones_cant = int(row[1])
             precio = float(row[2])
             costo_compra += cajones_cant * precio
    
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
        


       
       
       
       
       
       
       
       
       
       
       
       
       
    
    