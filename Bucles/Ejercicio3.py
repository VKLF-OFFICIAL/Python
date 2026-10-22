numero = int(input("Ingresa un número entero positivo >> "))
while numero <= 0:
    numero = int(input("El número debe ser positivo. Inténtalo de nuevo >> "))

for i in range(1,numero+1,2):
    print(str(i)+ ",",end="")