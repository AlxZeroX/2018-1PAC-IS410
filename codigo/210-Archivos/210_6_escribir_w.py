# Sobrescribe el archivo

with open('conteo.txt', 'w') as fhandler:
    for x in range(1, 10):
        fhandler.write(str(x) + '\n')
