fechaNAc = str(input("Ingresa tu fecha de nacimiento con el siguiente formato: dd/mm/aaaa >> "))
lista = fechaNAc.split("/")

print(f"Naciste el día {lista[0]} del mes {lista[1]} del año {lista[2]}.")