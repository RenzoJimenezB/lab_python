"""Diccionarios en Python"""

"""del: elimina un par key-value"""

var_1 = {
    "nombre": "Matías",
    "edad": 26,
    "promedio": 14
}

print(var_1)

var_1["distrito"] = "Lince"
del var_1["edad"]
del var_1["promedio"]

print(var_1)