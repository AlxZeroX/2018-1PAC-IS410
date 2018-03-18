'''
Para ocultar atributos y metodos se puede utilizar como prefijo el doble guion bajo (__), en este caso el elemento
queda oculto y solo es visible bajo el formato:
[nombre de objeto]._[Nombre de la clase]__[Atributo oculto]
'''

class Contador:
    def __init__(self):
        self.__cuenta = 0

    def contar(self):
        self.__cuenta += 1

    def imprimir(self):
        print(self.__cuenta)


c1 = Contador()
c1.contar()
c1.contar()

print('Valor original de la variable oculta')
c1.imprimir()

print('Se intenta modificar la variable oculta 206-Clases-abstractas 1000 directamente')
c1.__cuenta = 1000
c1.imprimir()

print('Se intenta modificar la variable oculta 206-Clases-abstractas 9999 utilizando el formato de revelado')
c1._Contador__cuenta = 9999
c1.imprimir()

print('Como quedo el objeto?')
print(c1.__dict__)