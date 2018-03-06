class Persona:
    poblacion = 0                   # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre        # Atributo de objeto
        Persona.poblacion += 1

p = Persona('Carlos')
q = Persona('Daniela')

# Acceder a atributo de objeto
print(p.nombre)

# Acceder a atributo de clase
print(p.poblacion)
print(Persona.poblacion)