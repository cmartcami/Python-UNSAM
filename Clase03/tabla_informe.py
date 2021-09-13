# -*- coding: utf-8 -*-
"""
@author: Camila Pc
En el Ejercicio 3.9, modificaste tu programa informe.py que calcula las ganancias o pérdidas de un camión que compra a productores y vende en el mercado. Copiá su contenido en un nuevo archivo tabla_informe.py y guarda éste también en la carpeta de ejercicios de esta clase. Ahora dejá el archivo informe.py, y trabajá sobre tabla_informe.py. Lo vas a modificar para producir una tabla como ésta:

 Nombre     Cajones     Precio     Cambio
---------- ---------- ---------- ----------
 Lima          100        32.2       8.02
 Naranja        50        91.1      15.18
 Caqui         150      103.44       2.02
 Mandarina     200       51.23      29.66
 Durazno        95       40.37      33.11
 Mandarina      50        65.1      15.79
 Naranja       100       70.44      35.84
En este informe, el "Precio" es el precio en el mercado y el "Cambio" es la variación respecto al precio cobrado por el productor.

Para generar un informe como el de arriba, primero tenés que recolectar todos los datos de la tabla. Escribí una función hacer_informe() que recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas conteniendo la información mostrada en la tabla anterior.

Agregá esta función a tu archivo tabla_informe.py.
"""
#Ejercicio 3.13 / 3.14

    
import csv
  
       
def leer_camion(nombre_archivo):   #Me devuelve una lista con diccionarios
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
    return camion

def leer_precios(nombre_archivo): #Me devuelve un diccionario con nombre y precio del producto.
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


       
def hacer_informe(nombre_archivo_camion, nombre_archivo_precio):
    with open('../Data/camion.csv', 'rt') as f:
       next(f)
       lista1 = []
       for line in f:
           row = line.split(',')
           producto1 = row[0]
           cajones1 = int(row[1])
           precio1 = float(row[2])
           buscar_precio(producto1)
           cambio1 = buscar_precio(producto1) - precio1 
           lista1.append((row[0], int(row[1]), float(buscar_precio(producto1)), float(cambio1)))
       return lista1

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:

        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}  {cambio:>10.2f}')
     
    
    
    
    
    
    
    
    
    
    
    
    
    