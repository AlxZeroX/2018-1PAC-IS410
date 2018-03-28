# Este programa devuelve el numero de lineas que existen en el archivo mbox.txt

contador = 0

try:
    fhandle = open('mbox-short.txt')
except FileNotFoundError:
    print('Archivo no existe')
else:
    for linea in fhandle:
        contador = contador + 1

    print(contador)
