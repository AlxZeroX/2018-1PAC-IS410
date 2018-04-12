import logging

# Establecer el nivel por defecto
logging.basicConfig(level=logging.DEBUG, filename="Alumno.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class Alumno:
    def __init__(self, cuenta, nombre, carrera):
        self.cuenta = cuenta
        self.nombre = nombre
        self.carrera = carrera

        logging.debug("Alumno creado: {}, {} de {}".format(self.nombre, self.cuenta, self.carrera))


if __name__ == '__main__':
    logging.info("Inicio programa")
    a1 = Alumno('Alberto', '1243234', 'Medicina')
    logging.info("Fin del programa")