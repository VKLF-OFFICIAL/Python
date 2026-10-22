vegetariano = str(input("La pizza es vegana? >> "))
VegaIngredientes = str("Pimiento y Tofu.")
NoVegaIngredientes = str("Peperoni ,Jamón y Salmón.")

if vegetariano in {"s", "si", "sí", "y", "yes", "S", "SI", "Si" ,"sI"}:
    print(f"Los ingredientes son {VegaIngredientes}")
    ingredienteAdiccional = str(input("La pizza viene con mozzarella y tomate puedes agregar un ingrediente de la lista anterior >> "))
else:
    print(f"Los ingredientes son {NoVegaIngredientes}")
    ingredienteAdiccional = str(input("La pizza viene con mozzarella y tomate puedes agregar un ingrediente de la lista anterior >> "))

print(f"La pizza lleva mozzarella y tomate {ingredienteAdiccional}.")