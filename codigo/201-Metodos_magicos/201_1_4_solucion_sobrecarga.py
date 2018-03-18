'''
Para el siguiente se hizo uso de dos funciones que inicializan de diversas formas al objeto.
De acuerdo al número de argumentos se llamará a una función específica.
'''

class Persona:
    # Metodo constructor
    def __init__(self, *args):
        size = len(args)

        if size == 1:
            self.inicializar_copia(*args)
        elif size == 3:      
            self.inicializar_simple(*args)
        else:   
            raise Exception('Numero de argumentos invalido')
        

    def inicializar_simple(self, nombre: str, identidad: str, lugar_nacimiento: str):
        self.nombre = nombre
        self.identidad = identidad
        self.lugar_nacimiento = lugar_nacimiento

    def inicializar_copia(self, copia):
        self.nombre = copia.nombre
        self.identidad = copia.identidad
        self.lugar_nacimiento = copia.lugar_nacimiento

    def __str__(self):
        return "Nombre: {}\nIdentidad: {}\nLugar Nacimiento: {}".format(self.nombre, self.identidad, self.lugar_nacimiento)


persona1 = Persona('Albert Eistein', '13430', 'Alemania')
persona1_copia = Persona(persona1)

print('Objeto persona1'.center(80, '-'))
print(persona1)

print('Objeto obtenido por el inicializador de copia'.center(80, '-'))
print(persona1_copia)