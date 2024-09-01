"""Listas en Python"""

"""copy(): Obtener todos los valores de una lista en otra variable"""

var_1 = ["SQL Server", "rDS", "MySQL", "PostgreSQL", "MariaDB"]
var_2 = var_1.copy()

print(f"El valor de 'var_2' es {var_2}")

var_2.append("SQLite3")
print(f"El valor de 'var_2' es {var_2}")

print(f"Los valores de 'var_1' son: {var_1}")