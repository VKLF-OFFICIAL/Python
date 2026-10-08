contraseñaAlma = "holabuenosdias123@"
contraseñaInsertada = input("Ingresa tu contraseña >> ")
contraseñaAlmaMinus = contraseñaAlma.lower()        #he pensado que para que no tenga que distinguir en mayusculas o minusculas se puede pasar la contraseña almacenada y la contraseña 
contraseñaMinus = contraseñaInsertada.lower()       #introducida por el usuario a minusculas y asi compararlas
if contraseñaAlmaMinus == contraseñaMinus :
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")