"""
Requisitos:

- Dentro de una empresa se solicita pedir nombre y apellido del empleado (input)
- Distrito de residencia
- Sueldo y cálculo del bono final del año que equivale al triple del sueldo mensual menos el 10% del sueldo
- Todos los datos deben ingresar en un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal el mensaje: "{Nombre} {Apellido} recibirá un {Bono} soles de bono de fin de año"

"""

usuario = input("Ingrese su nombre de usuario: ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sueldo = input("Ingrese su sueldo mensual: ")
distrito = input("Ingrese su distrito de residencia: ")

sueldo = float(sueldo)
bono = (sueldo * 3) - (sueldo * 0.1)

""""
my_dictionary = {}

my_dictionary["Usuario"] = usuario
my_dictionary["Nombre"] = nombre
my_dictionary["Apellido"] = apellido
my_dictionary["Distrito"] = distrito
my_dictionary["Bono"] = bono

print(my_dictionary)
"""

my_dictionary = {
    "Usuario": usuario,
    "Nombre": nombre,
    "Apellido": apellido,
    "Distrito": distrito,
    "Bono": bono
}

print(my_dictionary)

name = nombre
last_name = apellido
bonus = bono

print(f"{name} {last_name} recibirá {bonus} soles de bono de fin de año")
