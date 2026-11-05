palabra = str(input("Introduce una palabra >> "))
letra = str(input("Introduce una letra >> "))
contador = 0
for x in palabra[::1]:
    letraPalabra = x
    if letraPalabra == letra :
        contador = contador +1 
print(contador)
        