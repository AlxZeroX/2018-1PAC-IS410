import logging

# Establecer el nivel por defecto
logging.basicConfig(level=logging.DEBUG, filename="Alumno.log")

class Alumno:
    def __init__(self, cuenta, nombre, carrera):
        self.cuenta = cuenta
        self.nombre = nombre
        self.carrera = carrera

        logging.debug("Alumno creado: {}, {} de {}".format(self.nombre, self.cuenta, self.carrera))


if __name__ == '__main__':
    a1 = Alumno('Alberto', '1243234', 'Medicina')