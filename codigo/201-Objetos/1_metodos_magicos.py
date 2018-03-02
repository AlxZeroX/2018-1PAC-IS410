'''
Estos métodos no son, por lo general, llamados directamente
sino que, dependiendo de la situación, es posible que el interprete
los ejecute.
'''
class Persona:
    # Metodo constructor
    def __init__(self, nombre, identidad, lugar_nacimiento):
        self.nombre = nombre
        self.identidad = identidad
        self.lugar_nacimiento = lugar_nacimiento
        print('Metodo __INIT__ llamado al iniciar un objeto')

    def __del__(self):
        print('Metodo __DEL__ llamado al finalizar un objeto')

    # Metodo llamado cuando el objeto se comporta como un string:
    # Ej: cuando se manda a imprimir un objeto
    def __str__(self):
        return "Nombre: {}\nIdentidad: {}\nLugar Nacimiento: {}".format(self.nombre, self.identidad, self.lugar_nacimiento)


# Al crear el objeto es llamado __init__
persona1 = Persona('Allan Turing', '01201', 'Londres')

# Al tratar al objeto como str se llama al metodo __str__
print(persona1)

# Finalmente cuando el objeto Persona es destruido se llama al metodo __del__
persona1 = None
