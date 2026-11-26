"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
"""
numeros = []
for x in range (1,11):
    numero = x 
    numeros.append(numero)
print(numeros)
numeros.reverse()
print(numeros)