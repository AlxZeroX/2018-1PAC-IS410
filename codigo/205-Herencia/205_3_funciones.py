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

padre = Padre()
hijo = Hijo()
otro_hijo = OtroHijo()
nieto = Nieto()
otro_nieto = OtroNieto()

# Funcion isinstance
print('Objeto hijo es instancia de clase Hijo:',isinstance(hijo, Hijo))
print('Objeto nieto es instancia de clase Padre:', isinstance(nieto, Padre))

# Funcion issubclase
print('Clase OtroNieto es subclase de OtroHijo:', issubclass(OtroNieto, OtroHijo))
print('Clase OtroNieto es subclase de Padre:', issubclass(OtroNieto, Padre))
