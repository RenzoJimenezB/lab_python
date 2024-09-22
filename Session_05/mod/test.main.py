"""
- Crear un módulo donde se define una función
- La función obtiene el impuesto que va a pagar una persona
- El impuesto corresponde si el sueldo es mayor a S/500
- Impuesto: 8%
- Ingresar el sueldo por consola
"""

from tax_function import calculate_tax

salary = input(f"How much is your salary? ")

tax = calculate_tax(salary)
