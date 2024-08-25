"""
Requisitos:

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable
string con contenido numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string
3. Obtener y mostrar la suma de las 2 variables enteras
con la variable string y la variable flotante
4. Obtener y mostrar el módulo de las 2 variables enteras
5. Obtener y mostrar el resultado entero de las 2 variables enteras (//)

"""

# 1
var_num_1 = 100
var_num_2 = 200
var_float_1 = 10.5
var_float_2 = 2.2
var_str = "1000"
var_bool = True

# 2
suma_1 = var_num_1 + int(var_str)
print(f"El valor de 'suma_1' es {suma_1}")

#3
suma_2 = suma_1 + var_num_2 + var_float_1
print(f"El valor de 'suma_2' es {suma_2}")

#4
modulo_1 = var_num_1 % var_num_2
print(f"El valor de 'modulo_1' es {modulo_1}")

#5
result = var_num_1 // var_num_2
print(f"El valor de 'resultado' es {result}")
