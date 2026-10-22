numero = int(input("Ingresa un número entero positivo >> "))
while numero <= 0:
    numero = int(input("El número debe ser positivo. Inténtalo de nuevo >> "))
contador = numero 
while contador >= 0:
    print(contador)
    contador=contador-1
    