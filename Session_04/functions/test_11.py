"""Propiedades de string"""

"""
Requisitos
 
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_completo = nombre + " " + apellido
print(f"Longitud del nombre completo: {len(nombre_completo)}")

nombre_completo = nombre_completo.upper()
print(f"Nombre completo en mayúsculas: {nombre_completo}")

if len(nombre) > len(apellido):
    print("Su nombre es más largo que su apellido")
elif len(nombre) < len(apellido):
    print("Su apellido es más largo que su nombre")
else:
    print("Su nombre y apellido tienen la misma longitud")
