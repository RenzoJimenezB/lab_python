"""Condicional: if"""

edad_1 = int(input("Ingrese una primera edad: "))
edad_2 = int(input("Ingrese una segunda edad: "))

if edad_1 > edad_2:
    print("La edad 1 es mayor que la edad 2 que ha ingresado")
elif edad_2 == edad_1:
    print("Las edades ingresadas son iguales")
else:
    print("La edad 2 es mayor que la edad 1 que ha ingresado")
