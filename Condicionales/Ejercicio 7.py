ingresos = float(input("Ingresa tus ingresos >> "))
if ingresos <  10000:
    print("Tipo de impositivo es de  5%.")
else:
    if ingresos > 10000 and ingresos < 20000:
        print("Tipo de imposito es de 15%.")
    else:
        if ingresos > 20000 and ingresos < 35000:
            print("Tipo de imposito es de 20%.")
        else:
            if ingresos > 35000 and ingresos < 60000:
                print("Tipo de imposito es de 30%.")
            else:
                if ingresos > 60000:
                    print("Tipo de imposito es de 45%.")
                else:
                    print("El ingreso esta en un formato no correcto.")