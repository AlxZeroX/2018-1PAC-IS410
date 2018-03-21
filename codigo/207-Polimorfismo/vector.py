class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __add__(self, other):
        sumax = self.x + other.x
        sumay = self.y + other.y
        vector_suma = Vector(sumax, sumay)
        return vector_suma

    def __sub__(self, other):
        restax = self.x - other.x
        restay = self.y - other.y
        vector_resta = Vector(restax, restay)
        return  vector_resta

    def __radd__(self, other):
        raise NotImplementedError


def main():
    v1 = Vector(1, 0)
    v2 = Vector(0, 1)
    v3 = v1 + v2
    v4 = v3 - v2
    print('{} + {} = {}'.format(v1, v2, v3))
    print('{} - {} = {}'.format(v3, v2, v4))

    lista = [v1, v2, v3]
    print(sum(lista))

if __name__ == '__main__':
    main()