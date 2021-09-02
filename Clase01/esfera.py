# esfera.py
# ejercicio de la esfera

"""
En tu directorio de trabajo de esta clase, 
escribí un programa llamado esfera.py 
que le pida a le usuarie que ingrese por teclado el radio r de una esfera 
y calcule e imprima el volumen de la misma.
"""
from math import pi
radio = input('Ingrese radio:')
volumen = int(radio) ** 3 * 4/3 * pi
print(volumen)
