# Este programa devuelve las lineas que comienza con la palabra 'From '

contador = 0

try:
    fhandle = open('mbox-short.txt')
except FileNotFoundError:
    print('Archivo no encontrado')
else:
    for linea in fhandle:
        contador += 1
        if linea.startswith('From '):
            print("Linea {}: {}".format(contador, linea))
