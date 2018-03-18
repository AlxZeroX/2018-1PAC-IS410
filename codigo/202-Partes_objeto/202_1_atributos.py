class Persona:
    poblacion = 0                   # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre        # Atributo de objeto
        Persona.poblacion += 1

p = Persona('Carlos')
q = Persona('Daniela')

# Acceder 206-Clases-abstractas atributo de objeto
print(p.nombre)

# Acceder 206-Clases-abstractas atributo de clase
print('Atributo de clase desde el objeto:', p.poblacion)
print('Atributo de clase desde la clase:', Persona.poblacion)

# En caso de modificar un atributo de clase la forma 'objeto.atributo_clase' no funciona y crea un atributo de objeto
print('Se intento modificar el atributo de clase desde el objeto...')
p.poblacion = 100
print('Atributo de clase desde el objeto:', p.poblacion)
print('Atributo de clase desde la clase:', Persona.poblacion)