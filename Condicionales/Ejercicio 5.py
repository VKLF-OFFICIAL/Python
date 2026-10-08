edad = int(input("Ingresa tu edad >> "))
ingresos = float(input("Ingresa tus ingresos mensuales >> "))

if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")