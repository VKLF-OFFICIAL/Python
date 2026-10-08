sexo = str(input("Ingresa tu sexo H para hombre M para mujer >> "))
nombre = str(input("Ingresa tu nombre >> "))
letraNombre = nombre[0]
if (sexo == "M" and letraNombre < "M") or (sexo == "H" and letraNombre > "N"):
    print("A")
else:
    print("B")