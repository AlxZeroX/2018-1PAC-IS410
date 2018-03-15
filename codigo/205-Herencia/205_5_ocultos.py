class A:
    def __init__(self):
        self.__nombre = __class__

class B(A):
    def __init__(self):
        super().__init__()

    def acceder(self):
        print(self._A__nombre)

b = B()
b.acceder()
