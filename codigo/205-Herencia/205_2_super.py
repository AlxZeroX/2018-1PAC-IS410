class Padre:
    def saludar(self):
        print('Metodo del padre')

class Hijo(Padre):
    def saludo1(self):
        super().saludar()

    def saludo2(self):
        super(Hijo, self).saludar()


h0 = Hijo()
h0.saludo1()
h0.saludo2()

print(Hijo.mro())
