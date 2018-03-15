class Vaso:
    def __init__(self, capacidad):
        self.__contenido = 0
        self.capacidad= capacidad

    @property
    def contenido(self):
        return self.__contenido

    @contenido.setter
    def contenido(self, valor):
        if (valor > self.capacidad):
            self.__contenido = self.capacidad
        else:
            self.__contenido = valor

######################
vaso1 = Vaso(10)
vaso1.contenido = 8
print(vaso1.contenido)

print(vaso1.__dict__)