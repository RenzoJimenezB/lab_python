"""listas en Python"""

"""del(): Elimina un valor indicando el índice del valor en la lista"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canadá")
paises.append("España")
paises.append("Colombia")

print(f"Los valores de la lista son: {paises}")

del paises[2]
# del paises[5]

print(f"La lista actualizada tiene los valores: {paises}")
