"""Control o gestión de excepciones"""
from ast import Index

"""
- Crear una función aplicando excepciones
- El bloque 'except' debe considerar los errores de división entre 0 y tipo de valor
- Los valores deben ser ingresados por consola  
"""


def handle_exceptions():
    dividend = None
    divisor = None

    try:
        dividend = int(input("Provide a number to be used as dividend: "))
        divisor = int(input("Provide a number to be used as divisor: "))

        quotient = dividend / divisor
    except ZeroDivisionError:
        print(f"Cannot divide {dividend} by zero!")
    except TypeError:
        print(f"Cannot divide {type(dividend)} by {type(divisor)}!")
    except ValueError:
        print(f"Invalid input! Please enter numeric values for both dividend and divisor!")
    else:
        print(f"{dividend} / {divisor} equals {quotient}")


handle_exceptions()

"""
- Agregar una excepción donde se va a considerar una lista con 4 ítems
- Todos los datos de la lista debe ser strings
- Si se intenta modificar un índice no existente, crear un nuevo índice
- Dar al nuevo índice el valor de '0'
- Mostrar la lista final
"""

my_list = ["a", "b", "c", "d"]


def operate_on_list():
    index = int(input("Provide an index: "))
    value = input(f"Provide a value to replace index {index} value: ")

    try:
        my_list[index] = value
        print(my_list)
    except IndexError:
        print(f"Index {index} out of range!")
        my_list.append("0")
        print(my_list)


operate_on_list()


def remove_item():
    index = int(input("Provide an index: "))

    try:
        my_list.pop(index)
        print(my_list)
    except IndexError:
        print(f"Index {index} out of range!")


remove_item()
