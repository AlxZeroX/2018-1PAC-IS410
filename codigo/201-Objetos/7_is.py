class Persona:
    # Metodo constructor
    def __init__(self, *args):
        size = len(args)

        if size == 1:
            self.inicializarCopia(*args)
        elif size == 2:
            self.inicializarSimple(*args)
        else:
            raise Exception('Numero de argumentos invalido')

    def inicializarSimple(self, nombre: str, identidad: str):
        self.nombre = nombre
        self.identidad = identidad

    def inicializarCopia(self, copia):
        if isinstance(copia, Persona):
            self.nombre = copia.nombre
            self.identidad = copia.identidad
        else:
            raise Exception('El argumento no era de una Persona')

p = Persona('Fernando Ramirez', '12203443')
q = Persona(p)

# Verificar que son iguales
print('Ambos objetos son iguales:', p == q)

# Verificar si ambos objetos son el mismo
print('Ambos objetos son el mismo:', p is q)

# Cuando se copia un objeto de otro el resultado es el siguiente
q = p
print('Ambos objetos son iguales:', p == q)
print('Ambos objetos son el mismo:', p is q)

# Que pasa si se cambia el valor de un objeto
q.nombre = 'Copiado'
print(p.nombre)