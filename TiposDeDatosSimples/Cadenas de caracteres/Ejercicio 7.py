gmail = str(input("Ingresa tu correo >> "))
gsplit = gmail.split("@")
dominio = gsplit[1]
dominioRp = dominio.replace(dominio,"@ceu.es")

print(f"El correo es {gsplit[0]}{dominioRp}.")