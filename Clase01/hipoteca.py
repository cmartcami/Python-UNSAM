# hipoteca.py
# Ejercicio de hipoteca
"""
David solicitó un crédito a 30 años para comprar una vivienda, 
con una tasa fija nominal anual del 5%. Pidió $500000 al banco 
y acordó un pago mensual fijo de $2684,11.
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
Calcula el monto total que pagará David a lo largo de los años:

"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
meses = 0
ultimo_pago = 813.11


while saldo > 0:
    meses = meses + 1
    if 61 <= meses <= 108:
      saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
      total_pagado = total_pagado + pago_mensual + pago_extra
      print(meses, int(total_pagado), int(saldo))
    elif meses > 309:
         saldo = saldo * (1+tasa/12) - ultimo_pago
         total_pagado = total_pagado + ultimo_pago
         print(meses, int(total_pagado), int(saldo))       
    else:
         saldo = saldo * (1+tasa/12) - pago_mensual
         total_pagado = total_pagado + pago_mensual
         print(meses, int(total_pagado), int(saldo))
         
         

print('Total pagado', round(total_pagado, 2))
print('Meses requeridos', meses)
int(total_pagado)
int(saldo)