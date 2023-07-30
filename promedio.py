# Mis disculpas por el error en la interpretación. Entendido, comprarás un 25% más al precio de 0.08193 una vez que el precio caiga un 1.5%. Vamos a calcular el nuevo precio promedio en base a esta información.

# Paso 1: Calcular el precio de compra inicial
# Tienes X CANTIDAD DE MONEDAS (220) y el precio de compra inicial es de Y PRECIO( 0.08318)


Monedas_inicio = float(input("Ingresa las monedas iniciales:"))
precio_entrada = float(input("Ingresa el precio de entrada: "))


Costo_inicial = Monedas_inicio * precio_entrada



# Paso 2: Calcular el número de unidades adicionales a comprar
# Para calcular el 25% de las unidades iniciales, multiplicamos el número inicial por 0.25:

# 25% de 220 TRX = 220 TRX * 0.25 = 55 TRX

porcentajeAdCripto = int(input("Ingresa el porcentaje adicional de monedas a comprar: "))
adecimal = porcentajeAdCripto / 100
monedasAdicionales = Monedas_inicio * adecimal

if monedasAdicionales.is_integer():
    print(f"Las monedas adicionales son: {int(monedasAdicionales)}")
else:
    print(f"Las monedas adicionales son: {monedasAdicionales}")




# Paso 3: Calcular el costo de las nuevas unidades
# El precio al que comprarás las nuevas unidades es de 0.08193.

nuevoPrecio = float(input("Ingresa el precio de la recompra: "))

# Costo de las nuevas unidades = 55 TRX * 0.08193 = 4.50515
usdtaditcripto = monedasAdicionales * nuevoPrecio

# Paso 4: Calcular el nuevo costo total
# Ahora sumamos el costo inicial y el costo de las nuevas unidades:

# Nuevo costo total = Costo inicial + Costo de las nuevas unidades
# Nuevo costo total = 18.2996 + 4.50515 = 22.80475
CostoTotal = Costo_inicial + usdtaditcripto

# Paso 5: Calcular el nuevo número total de unidades
# Agregamos las nuevas unidades al número total de unidades:

# Nuevo número total de unidades = 220 TRX + 55 TRX = 275 TRX

totalCriptos = Monedas_inicio + monedasAdicionales
# Paso 6: Calcular el nuevo precio promedio
# Finalmente, calculamos el nuevo precio promedio:

# Nuevo precio promedio = Nuevo costo total / Nuevo número total de unidades
# Nuevo precio promedio = 22.80475 / 275 ≈ 0.083112

NuevoPrecioPromedio = CostoTotal / totalCriptos
round(NuevoPrecioPromedio)

print(f"El precio promedio una vez que toque la siguiente recompra sería {round(NuevoPrecioPromedio, 5)}")
# El nuevo precio promedio sería aproximadamente 0.083112, o simplemente redondeado a 0.08311 dependiendo de la cantidad de decimales que desees utilizar. Recuerda que los cálculos pueden variar ligeramente dependiendo de cómo se manejen los decimales y redondeos en la plataforma de trading o cálculos financieros que utilices.