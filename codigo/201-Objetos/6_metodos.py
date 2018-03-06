class Persona:
    # Atributo de objeto
    poblacion = 0

    # Inicializador. Es un metodo de objeto
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.poblacion += 1

    # Metodo de clase el primer argumento indica la clase misma
    @classmethod
    def conteo_personas(cls):
        print("Poblacion actual:", cls.poblacion)

    # Metodo estatico. No necesita ningun argmumento inicial
    @staticmethod
    def reiniciar_poblacion():
        Persona.poblacion = 0


p = Persona('Erika')
p.conteo_personas();
Persona.reiniciar_poblacion();
Persona.conteo_personas();