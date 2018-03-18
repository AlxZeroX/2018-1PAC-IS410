import figura


class Cuadrado(figura.Figura2D):
    def __init__(self, longitud):
        super(Cuadrado, self).__init__(4, longitud)

    def calcular_area(self):
        return self.longitud ** 2

    def dibujar(self):
        super().dibujar()
        #print('Cuadrado')


if __name__ == '__main__':
    cuadrado = Cuadrado(4)
    print('El perimetro del cuadrado es:', cuadrado.calcular_perimetro())
    area = cuadrado.calcular_area()
    print('El area de un cuadrado con un largo de {} es = {}'.format(cuadrado.longitud, area))
