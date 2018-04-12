import logging

# Establecer el nivel por defecto
logging.basicConfig(level=logging.DEBUG)

logger1 = logging.getLogger('Alumno')
logger2 = logging.getLogger('Main')

class Alumno:
    def __init__(self, cuenta, nombre, carrera):
        self.cuenta = cuenta
        self.nombre = nombre
        self.carrera = carrera

        logger1.debug("Alumno creado: {}, {} de {}".format(self.nombre, self.cuenta, self.carrera))


if __name__ == '__main__':
    a1 = Alumno('Alberto', '1243234', 'Medicina')
    logger2.debug('Fin del programa')