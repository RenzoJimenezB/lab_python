"""Listas en Python"""

"""count(value): Cantidad de veces que aparece un elemento"""

var_1 = ["Python", "Java", "PHP", "Javascript", "TypeScript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("python")
var_1.append("Python")

print(f"La lista actualizada tiene los siguientes valores: {var_1}")

print(f"La cantidad de veces que se repite 'Python' es {var_1.count('Python')}")
print(f"La cantidad de veces que se repite 'Java' es {var_1.count('Java')}")