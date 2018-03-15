'''
Esta es otra forma de representar propiedades en Python
'''
class Vaso:
    def __init__(self, capacidad):
        self.__contenido = 0
        self.capacidad = capacidad

    def get_contenido(self):
        return self.__contenido

    def set_contenido(self, valor):
        if (valor > self.capacidad):
            self.__contenido = self.capacidad
        else:
            self.__contenido = valor

    # Crea una propiedad con la secuencia: getter, setter, deletter, docstring de la propiedad
    contenido = property(get_contenido, set_contenido)

######################
vaso1 = Vaso(10)
vaso1.contenido = 8
print(vaso1.contenido)

print(vaso1.__dict__)