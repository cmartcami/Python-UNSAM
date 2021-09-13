# -*- coding: utf-8 -*-
"""
Escribí un programa tablamult.py que imprima de forma prolija 
las tablas de multiplicar del 1 al 9 usando f-strings. Si podés, 
evitá usar la multiplicación, usando sólo sumas alcanza.
"""
print(' ', end = ' ')
for i in range(0,10):
    print(f'{i:>4d}', end='')
print('')  
print('-'*44)

for i in range(10):
    print(i, end=': ')
    for j in range(0,10):
        print(f'{i*j:>3d}', end='\t')
        
    print('')
    