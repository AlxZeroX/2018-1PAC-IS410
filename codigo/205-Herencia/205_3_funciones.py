class A:
    def saludar(self):
        print(__class__)

class B(A):
    def saludar(self):
        super().saludar()

class C(A):
    # Metodo Redefinido
    def saludar(self):
        print(__class__)

class D(B):
    def saludar(self):
        super().saludar()

class E(C):
    pass

print(D.mro())

a = A()
b = B()
c = C()
d = D()
e = E()

a.saludar()
b.saludar()
c.saludar()
d.saludar()
e.saludar()


# Funcion isinstance
print('Objeto b es instancia de clase B:', isinstance(b, B))
print('Objeto d es instancia de clase A:', isinstance(d, A))

# Funcion issubclase
print('Clase E es subclase de C:', issubclass(E, C))
print('Clase E es subclase de A:', issubclass(E, A))