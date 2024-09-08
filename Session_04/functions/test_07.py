"""Condicional if"""
"""if ternarios"""

"""
Requisitos:
- Ingresar por teclado el sueldo de un empleado
- Si el sueldo es mayor a 3500, imprimir "Su sueldo no tiene bonificación"
- Caso contrario: "Su sueldo tiene bonificación este año y será de: {}"
- Sueldo_final = sueldo + sueldo * 0.2
"""

sueldo = int(input("Ingrese su sueldo mensual: "))

if sueldo > 3500:
    print("Su sueldo no tiene bonificación")
else:
    sueldo_final = sueldo + (sueldo * 0.2)
    print(f"Su sueldo tiene bonificación de {sueldo * 0.2}. Este año su sueldo final será de: {sueldo_final}")
