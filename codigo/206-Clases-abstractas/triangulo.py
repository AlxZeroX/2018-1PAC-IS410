import figura


class Triangulo(figura.Figura2D):
    def __init__(self, longitud):
        super().__init__(3, longitud)


if __name__ == '__main__':
    # No puede crear el objeto tipo Triangulo debido a que no se ha implementado el metodo 'calcular_area'
    triangulo = Triangulo(5)
