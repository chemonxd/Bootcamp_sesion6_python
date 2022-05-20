
class Alumno:
    nombre = "Jose Juan Jimenez Jara"
    nota = 9.0

    def ingresar_valores(self):
        print("ingrese el nombre del alumno por favor")
        self.nombre = input()
        print("ingrese la nota del alumno")
        self.nota = float(input())

    def validar_calificación(self):
        if self.nota >= 6:
            print("la nota de ", self.nombre, " es aprobatoria")
        else:
            print("la nora de ", self.nombre, " es NO aprobatoria")


ejecutar = Alumno()
ejecutar.ingresar_valores()
ejecutar.validar_calificación()
