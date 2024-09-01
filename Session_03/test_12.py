"""Listas en Python"""

"""
Requisitos:

1. Crear 2 listas vacías
2. Agregar datos de nombre, edad y profesión para ambos
3. Obtener y mostrar la suma de las edades
4. Sumar ambas listas y mostrar el resultado en la terminal
5. Mostrar de manera inversa la suma de ambas listas
6. Actualizar la nueva lista eliminando las edades de ambas personas

"""

lista_1 = []
lista_2 = []

lista_1.append("Renzo")
lista_1.append(25)
lista_1.append("estudiante")

lista_2.append("Carlos")
lista_2.append(99)
lista_2.append("contador")

suma_edades = lista_1[1] + lista_2[1]
print(f"La suma de las edades de {lista_1[0]} y {lista_2[0]} es: {suma_edades}")

suma_listas = lista_1 + lista_2
print(f"El resultado de sumar ambas listas es: {suma_listas}")

suma_listas.reverse()
print(f"El resultado de invertir la suma de ambas listas es: {suma_listas}")

del suma_listas[1]
del suma_listas[3]
print(f"La lista actualizada sin edades tiene los siguientes valores: {suma_listas}")


