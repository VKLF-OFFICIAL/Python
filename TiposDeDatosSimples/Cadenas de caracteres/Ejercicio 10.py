Compra = str(input("Ingresa la lista de la compra separadas por ','. \n Ejemplo: Leche,Cereales,etc. >> "))
lista = Compra.split(",")

for Compra in lista:
    print(f"·{Compra}")