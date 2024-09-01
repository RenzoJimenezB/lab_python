"""Diccionarios en Python"""

"""Key names always go in lowercase"""


var_1 = {
    "nombre": "Matías",
    "edad": 26,
    "promedio": 14
}

print(f"El diccionario tiene el siguiente contenido: {var_1}")

"""Agregar elementos en un nuevo key"""

var_1["distrito"] = "San Isidro"
var_1["habilitado"] = True

print(f"El diccionario actualizado tiene los siguientes valores: {var_1}")