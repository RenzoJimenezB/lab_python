"""Propiedades de string"""

"""String Methods"""

cadena_1 = "Connection to a DB with Python"
cadena_2 = cadena_1.replace(cadena_1[0:10], "New connection")
print(cadena_2)

cadena_3 = "     " + cadena_1 + "     "
print(cadena_3)

cadena_4 = cadena_1.rstrip()
print(cadena_4)

cadena_5 = cadena_3.lstrip()
print(cadena_5)
