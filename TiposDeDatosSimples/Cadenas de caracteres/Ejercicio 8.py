precio = input("ingresa un precio con dos sus centimos >> ")
lista = str(precio).split(".")
print(f"El precio es de {lista[0]} euros y {lista[1]} centimos.")