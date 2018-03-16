import abc


class Figura2D(metaclass=abc.ABCMeta):
    def __init__(self, numero_lados, longitud):
        self.numero_lados = numero_lados
        self.longitud = longitud

    def calcular_perimetro(self):
        return self.longitud * self.numero_lados

    @abc.abstractclassmethod
    def calcular_area(self):
        '''Calcula el area de una figura regular'''

    # @abc.abstractclassmethod
    # def dibujar(self):
    #    print('Figura 2D')


if __name__ == '__main__':
    fig = Figura2D(0, 0)
