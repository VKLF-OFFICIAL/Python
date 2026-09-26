interesAnual = float(1.04)
cDineroDepositado = float(input("Ingresa la cantidad de dinero depositada >> "))

primeraño = round(cDineroDepositado * interesAnual,2)
segundoaño = round(primeraño * interesAnual,2)
terceraño = round(segundoaño * interesAnual,2)

print("Cantidad ahorrada en los tres futuros años: ")
print(f"El primer año se ahorrara {primeraño}€.")
print(f"El segundo año se ahorrara {segundoaño}€.")
print(f"El tercer año se ahorra1ra {terceraño}€.")