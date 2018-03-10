class Padre:
    def saludar(self):
        print('Hola... desde', __class__)

class Hijo(Padre):
    def saludar(self):
        super().saludar()

class OtroHijo(Padre):
    # Metodo Redefinido
    def saludar(self):
        print('Hola (redefinido)... desde', __class__)

class Nieto(Hijo):
    def saludar(self):
        super().saludar()

class OtroNieto(OtroHijo):
    pass

print('Hijo'.center(80, '-'))
hijo = Hijo()
hijo.saludar()

print('Otro Hijo'.center(80, '-'))
hijo2 = OtroHijo()
hijo2.saludar()

print('Nieto'.center(80, '-'))
nieto = Nieto()
nieto.saludar()

print('Otro Nieto'.center(80, '-'))
nieto2 = OtroNieto()
nieto2.saludar()


# Verificar el Method Resolution Order (mro)
print(Nieto.mro())