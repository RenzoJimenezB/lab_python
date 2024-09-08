class Alumno:
    nacionalidad = "Peruano"

    def __init__(self, nombre, nota_1=0, nota_2=0, nota_3=0):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.promedio = 0
        self.aprobado = False

    def get_grade(self):
        self.promedio = sum([self.nota_1, self.nota_2, self.nota_3]) / 3
        if self.promedio >= 13:
            self.aprobado = True

    def get_info(self, distrito):
        return {
            "nombre": self.nombre,
            "distrito": distrito,
        }


alumno_1 = Alumno("Carlos", 10, 12, 13)
alumno_1.get_grade()
print(f"El promedio del alumno es: {alumno_1.promedio}")
print(f"El alumno está aprobado: {alumno_1.aprobado}")

alumno_1_info = alumno_1.get_info("Santiago de Surco")
print(f"Información de alumno: {alumno_1_info}\n")

alumno_2 = Alumno("Pepe", 18, 17, 20)
alumno_2.get_grade()
print(f"El promedio del alumno es: {alumno_2.promedio}")
print(f"El alumno está aprobado: {alumno_2.aprobado}")

alumno_2_info = alumno_2.get_info("San Borja")
print(f"Información de alumno: {alumno_2_info}")
