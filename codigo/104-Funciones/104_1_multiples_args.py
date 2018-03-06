def sumar(a, b):
    print(a + b)

''' 
Para el caso anterior solo es posible utilizar dos parametros para utilizar la suma. Si se necesitara que la funcion
permitiera mas de dos argumentos es necesario la siguiente construccion: *args.
Internamente se tiene una tupla la cual puede ser utilizada para manipular los multiples argumentos
'''
def sumar_multiple(*args):
    print(sum(args))

sumar_multiple(1)
sumar_multiple(1, 2, 3)
sumar_multiple(1, 2, 3, 4, 5)


''' 
Tambien es posible utilizar un diccionario para ello se utiliza la siguiente definicion: **kwargs
'''
def imprimir_argumentos(**kwargs):
    for clave, valor in kwargs.items():
        print('Clave:', clave, 'Valor:', valor)

imprimir_argumentos(a = 'Hola', b = 'Mundo')