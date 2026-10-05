articulo = str(input("Ingresa el nombre del articulo >> "))
precio = float(input("Ingresa el precio del articulo >> "))
unidades = int(input("Ingresa el número de unidades del articulo >> "))
costeT = precio * unidades
print(f"El articulo {articulo} tiene un precio de {precio:09.2f}€ y hay {unidades:03d} unidades y un precio total de {costeT:011.2f}€ ")