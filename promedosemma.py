monedas = int(input("Ingresa las monedas iniciales: "))
precio = float(input("Ingresa el precio de entrada: "))

monedasAdicional = float(input("Ingresa las monedas totales de la segunda recompra: "))
preciomAdicionals = float(input("Ingresa el precio de la segunda recompra: "))


resultado = ((precio * monedas) + (preciomAdicionals * monedasAdicional)) / (monedas + monedasAdicional)

print(f"Precio promedio: {round(resultado, 5)}")


















# Tienes
# 220 TRX
# a precio
# 0.08318

# Después se le agregara lo siguiente
# 308 TRX
# a precio de
# 0.08193


# ocupamos la siguiente formula
# ((Precio 1 X tamaño 1) + (Precio 2 X tamaño 2) ) / (tamaño 1 + tamaño 2)
# ((0.08318 X 220) + ( 0.08193 X 308)) / (220 + 308)
# (18.2996 + 25.23444) / 528
# 43.53404 / 528

# 0.08245083333

# entonces quedaria una posición con tamaño de
# 528 TRX
# con precio de entrada de
# 0.08245
