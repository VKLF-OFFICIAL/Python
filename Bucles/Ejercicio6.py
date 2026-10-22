"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
numero = int(input("Ingresa un número entero  >> "))
contador = 1
asterisco = "*"
while contador <= numero:
    print(asterisco) 
    asterisco= asterisco + "*"
    contador= contador+1

