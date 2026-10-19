inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
dineroBase = 2400

valoracion = float(input("Ingresa la valoración del trabajador >> "))

if valoracion == inaceptable:
    dinero = dineroBase * valoracion
elif valoracion == aceptable:
    dinero = dineroBase * valoracion
elif valoracion >= meritorio:
    dinero = dineroBase * valoracion
else:
    print("Valor ingresado no válido.")
print(f"El dinero que recibirá es {dinero} €.")