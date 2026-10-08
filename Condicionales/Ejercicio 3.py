#Estaba haciendo el ejercicio y al ir a crear una variable llamada division me ha salido la ayuda de relleno de ZeroDivisionError
a = float(input("Ingresa el valor A de la operación >> "))
b = float(input("Ingresa el valor B de la operación >> "))

if b == 0:
    print("El divisor es 0 , cambialo.")
else:
    division = a / b
    print(f"El resultado es {division}")
