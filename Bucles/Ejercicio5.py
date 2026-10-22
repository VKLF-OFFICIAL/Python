cantidad = float(input("Ingresa la cantidad invertir >> "))
interesAnual = float(input("Ingresa el interes anual >> "))
años = int(input("Ingresa la cantidad de años a invertir >> "))

for año in range(1, años + 1):
    capital_obtenido = cantidad * (1 + interesAnual / 100) ** año
    print(f"Año {año}: {capital_obtenido:.2f} €.")
