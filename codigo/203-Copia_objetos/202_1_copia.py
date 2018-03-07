import auto

auto1 = auto.Auto('Toyota', 'Corolla', 2016)

# Referencia del objeto 'auto1' hacia 'auto2'
auto2 = auto1

''' 
Si es modificado un objeto (por medio de la referencia y la indicaciones de que los objetos creados por el usuario son,
por lo general, objetos mutables) el otro se modifica
'''

auto2.marca = 'Marca modificada'
print('Marca del objeto 1, el cual no fue modificado directamente:', auto1.marca)

print('Objetos iguales:', auto1 == auto2)
print('Objetos referencian la misma direccion:', auto1 is auto2)