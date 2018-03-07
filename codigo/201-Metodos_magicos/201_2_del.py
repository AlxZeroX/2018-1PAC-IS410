
class Persona:
    def __del__(self):
        print('Metodo __DEL__ llamado al finalizar un objeto')

persona1 = Persona()

# Cuando el objeto Persona es destruido se llama al metodo __del__
persona1 = None
print('Fin del programa'.center(80, '-'))
