# Esta clase padre o base
class Persona:
    def __init__(self, nombre, identidad):
        self.nombre = nombre
        self.identidad = identidad

    def __str__(self):
        return "Nombre: {}  Identidad: {}".format(self.nombre, self.identidad)


class Estudiante(Persona):
    def matricular(self, cuenta, carrera, centro_estudios):
        self.cuenta = cuenta
        self.carrera = carrera
        self.centro_estudios = centro_estudios


    # Redefinir (reescribir) un metodo heredado
    def __str__(self):
        str_base = super().__str__()
        str_derivada = "\nCuenta: {}. Carrera: {}. Centro: {}".format(self.cuenta, self.carrera, self.centro_estudios)

        return str_base + str_derivada

p0 = Estudiante('Alberto Castro', '1234')
p0.matricular('3243242', 'Ing. Sistemas', 'CU')
print(p0)