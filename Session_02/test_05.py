"""
Requisitos:

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables de remuneración de enero y febrero
3. Crear 1 variable donde se sumará el ingreso de los meses de enero y febrero
4. Mostrar en pantalla el mensaje 'Hola, soy {nombre}. Mi profesión es {profesión] y mi remuneración acumulada es de {total}"
"""

nombre = "Renzo"
profesion = "estudiante"
ciudad = "Huanuco"

totalEnero = 5000
totalFebrero = 6000
totalRemuneracion = totalEnero + totalFebrero

print("Hola, soy {}. Mi profesión es {} y mi remuneración acumulada es {}".format(nombre, profesion, totalRemuneracion))