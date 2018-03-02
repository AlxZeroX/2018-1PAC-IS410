# Python no maneja la sobrecarga como otros lenguajes

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __init__(self, nombre, identidad):
        self.nombre = nombre
        self.identidad = identidad

persona1 = Persona('Ana')