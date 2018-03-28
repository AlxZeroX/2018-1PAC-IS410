# Uso del operador with como Context Manager. En este caso no es necesario cerrar el archivo

with open('mbox.txt') as fhandler:
    lineas = fhandler.readlines()

    numeroLineas = len(lineas)
    print('El total de lineas es', numeroLineas)
    print(fhandler)
