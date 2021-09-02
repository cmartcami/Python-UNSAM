# rebotes.py

"""
Una pelota de goma es arrojada desde una altura de 100 metros
y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa rebotes.py que imprima una tabla 
mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.
"""

altura_inicial = 100 * 3/5 #Altura en Metros
rebote = 1

while rebote <= 10:
	print(rebote, altura_inicial)
	rebote = rebote + 1
	altura_inicial = altura_inicial * 3 / 5
