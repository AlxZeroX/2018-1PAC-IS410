'''
Programa que escribe un str en un archivo
Los 3 modos más comúnes para abrir un archivos son:
    'r' solo lectura
    'w' escritura (sobrescritrua)
    'a' escritura (escribe al final)
'''

with open('conteo.txt', 'w') as fhandler:
    for x in range(1, 10):
        fhandler.write(str(x) + '\n')
