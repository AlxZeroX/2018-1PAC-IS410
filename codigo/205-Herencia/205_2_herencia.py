class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

class Taxi(Auto):
    def __init__(self, marca, modelo, año, numero):
        # No se necesita redefinir otra vez el inicializador de los 3 primeros atributos
        super().__init__(marca, modelo, año)
        self.numero = numero


taxi1 = Taxi('Datsun', '210', 1980, '1245')
