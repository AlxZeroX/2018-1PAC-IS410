class Libro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    # Este funciona para el operador (+)
    def __add__(self, other):
        return self.paginas + other.paginas

    def __sub__(self, other):
        return self.paginas - other.paginas

    # def __radd__(self, other):
    #    return self.paginas + other


if __name__ == '__main__':
    libro1 = Libro('Fahrenheit 451', 200)
    libro2 = Libro('Python para todos', 130)

    print(libro1 + libro2)
    print(libro1 - libro2)

    # print(sum([libro1, libro2]))
