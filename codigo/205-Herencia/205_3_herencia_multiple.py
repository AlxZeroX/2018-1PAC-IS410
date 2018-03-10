class A:
    def __init__(self):
        print('A')

class B:
    def __init__(self):
        print('B')

class C(B):
    def __init__(self):
        print('C')
        #super().__init__()

class D(B, C, A):
    pass

print(D.mro())
d0 = D()