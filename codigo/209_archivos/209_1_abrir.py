# En modo lectura si el archivo se intenta abrir y no existe, hay un error

try:
    lectura = open('lectura.txt', 'r')
except Exception as ex:
    print(ex)
else:
    print('El archivo se abrio')
    print(lectura)

# En modo escritura (W o A) en caso de no existir el archivo se crea.
escritura = open('escritura.txt', 'w')
print(escritura)
