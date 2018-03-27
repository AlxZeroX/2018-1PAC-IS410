# Uso del operador with como Context Manager

with open('mbox.txt') as fhandler:
    lineas = fhandler.readlines()

    numeroLineas = len(lineas)
    print('El total de lineas es', numeroLineas)
    print(fhandler)
