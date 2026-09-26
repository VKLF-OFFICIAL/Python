p_payaso = int(112)
p_muñeca = int(75)

cantidad_payaso = int(input("Ingresa la cantidad de payasos vendidos en el pedido actual >> "))
cantidad_muñeca = int(input("Ingresa la cantidad de muñecas vendidos en el pedido actual >> "))

p_t_payaso = cantidad_payaso * p_payaso
p_t_muñeca = cantidad_muñeca * p_muñeca
p_total = p_t_muñeca + p_t_payaso
print(f"El peso total es {p_total} g  de los cuales  {p_t_payaso} g son de payasos y {p_t_muñeca} g de muñecas.")