class Pato:
    def graznar(self):
        print('Cuac!')


class FalsoPato:
    def graznar(self):
        print('Cuac! (falso)')


# Funcion probar metodos similares en objetos que no tienen relacion de herencia
def hacer_graznar(objeto):
    objeto.graznar()


pato1 = Pato()
pato2 = FalsoPato()

hacer_graznar(pato1)
hacer_graznar(pato2)
