"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.
"""

palabra = str(input("Ingresa una palabra para saber si es un palindromo >> "))
prueba = str()
for i in palabra [::-1 ]:
    prueba = prueba + i
print(prueba)
if prueba == palabra :
    print("Es palindromo.")

else:
    print("No es palindromo.")