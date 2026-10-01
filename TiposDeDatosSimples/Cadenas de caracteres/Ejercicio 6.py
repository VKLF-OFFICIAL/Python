frase = str(input("Ingresa uan frase >> "))
letra = str(input("Ingresa una letra >> "))

letraU = letra.upper()

reple = frase.replace(letra , letraU)
print(f"{reple}")