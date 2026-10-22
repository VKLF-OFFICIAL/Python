edadUsu = int(input("Ingresa tu edad >> "))
if edadUsu < 4 :
    print("La entrada es GRATIS.")
elif edadUsu > 4 and edadUsu < 18: 
    print("La entrada es 5 €.")
else:
    print("La entrada es 10 €.")