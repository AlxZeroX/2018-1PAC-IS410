import copy
import auto

auto1 = auto.Auto('Toyota', 'Rav-4', 2010)

# Crear un clon del objeto 'auto1' utilizando el modulo 'copy'
auto2 = copy.copy(auto1)

print('Auto 1'.center(80, '-'))
print(auto1)
print('Auto 2'.center(80, '-'))
print(auto2)

print('Objetos iguales:', auto1 == auto2)
print('Objetos referencian la misma direccion:', auto1 is auto2)