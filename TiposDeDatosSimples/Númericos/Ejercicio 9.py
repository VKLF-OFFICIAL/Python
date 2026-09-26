cantidad = float(input("Ingrese la cantidad a invertir >> "))
interesAnual = float(input("Ingrese la interes anual >> "))
añosInvertir = float(input("Ingrese los años de la inversión >> "))

resultado = round (cantidad *(1 + interesAnual / 100) ** añosInvertir,2)
print(f"El capital final es de {resultado} € .")