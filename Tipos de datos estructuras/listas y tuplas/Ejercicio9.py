"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
"""
palabra = str(input("Ingresa una palabra para saber cuantas veces aparece cada vocal >> "))
a = 0
e = 0
i = 0
o = 0
u = 0 

for x in palabra.lower():
    if x == "a":
        a = a + 1
    elif x == "e":
        e = e + 1
    elif x == "i":
        i = i + 1
    elif x == "o":
        o = o + 1
    elif x == "u":
        u = u + 1

print(f"A : {a} E : {e} I : {i} O : {o} U : {u}")
    