pan = float(3.49)
descuento = float(0.6)

cantidadBarras = int(input("Introduce la cantidad de barras que quiere >> "))
precioBarras = cantidadBarras * pan
panDescuento = precioBarras * descuento

print(f"El precio de las barras de pan sin descuento es {precioBarras}€. \n El precio de las barras de pan con descuento es de {panDescuento}€.")