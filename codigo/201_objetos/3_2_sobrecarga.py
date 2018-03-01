class Persona:
    # Metodo constructor
    def __init__(self, *args):
        size = len(args)

        if size == 1:
            self.inicializarCopia(*args)
        elif size == 3:      
            self.inicializarSimple(*args)

    def inicializarSimple(self, nombre: str, identidad: str, lugar_nacimiento: str):
        self.nombre = nombre
        self.identidad = identidad
        self.lugar_nacimiento = lugar_nacimiento

    def inicializarCopia(self, copia):
        self.nombre = copia.nombre
        self.identidad = copia.identidad
        self.lugar_nacimiento = copia.lugar_nacimiento


    def __str__(self):
        return "Nombre: {}\nIdentidad: {}\nLugar Nacimiento: {}".format(self.nombre, self.identidad, self.lugar_nacimiento)


persona1 = Persona('Albert Eistein', '13430', 'Alemania')
persona1_copia = Persona(persona1)

print(persona1)
print(persona1_copia)

# Comprobar si los dos objetos son iguales
print(persona1 == persona1_copia)

# Comprobar si ambos objetos son el mismo
print(persona1 is persona1_copia)