"""Bucle for"""

ingenierias = ["Software", "Sistemas", "Industrial", "Química", "Mecánica", "Mecatrónica"]

print(f"El tamaño de la lista es de: {len(ingenierias)} ítems ")
i = 0

for ingenieria in ingenierias:
    print(f"Nombre de la ingeniería: {ingenieria}")
    i += 1
    print(f"Iteración {i}")
