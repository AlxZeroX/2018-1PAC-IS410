class A:
    def __init__(self):
        print('A')

class B:
    def __init__(self):
        print('B')

    def func_b(self):
        print('Funcion unica de B')

class C(B):
    def __init__(self):
        print('C')
        #super().__init__()

class D(A, C, B):
    pass

print(D.mro())
d0 = D()
d0.func_b()
