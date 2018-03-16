import figura


class Triangulo(figura.Figura2D):
    def __init__(self, longitud):
        super().__init__(3, longitud)


if __name__ == '__main__':
    triangulo = Triangulo(5)
