"""Input y Output"""

usuario = input("Ingrese su nombre de usuario: ")
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print(f"Su usuario es: {usuario}")
print(f"Bienvenido/a, {nombre}!")

updated_age = int(edad) + 5
print(f"Su edad actualizada es: {updated_age}")
