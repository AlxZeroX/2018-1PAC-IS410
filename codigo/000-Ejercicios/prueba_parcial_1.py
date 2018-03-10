import parcial_1

print('Prueba 1.1:', parcial_1.hallarPalabraMayor(['hola', 'valor', 'piedra', '']) == 'piedra')
print('Prueba 1.2:', parcial_1.hallarPalabraMayor([]) == '')
print('Prueba 1.3:', parcial_1.hallarPalabraMayor(['aa', 'bb', 'aa']) == 'bb')
print('Prueba 1.4:', parcial_1.hallarPalabraMayor([1, 2, 3]) == '3')

print('Prueba 2.1: ', parcial_1.hallarPares([1, 2, 3, 4]) == 2)
print('Prueba 2.2: ', parcial_1.hallarPares([]) == 0)
print('Prueba 2.3: ', parcial_1.hallarPares(['a', 'b', 2]) == 0)

print('Prueba 3.1', parcial_1.generarArmonicos(3) == '1 + 1/2 + 1/3')

print(parcial_1.obtenerEdad('0801-1990-12345') == 28)

print('Prueba 5.1: ', parcial_1.obtenerDigitoMasSignificativo(123) == 1)
print('Prueba 5.2: ', parcial_1.obtenerDigitoMasSignificativo(4545) == 4)
print('Prueba 5.3: ', parcial_1.obtenerDigitoMasSignificativo('hola') == 0)

print('Prueba 6.1:', parcial_1.conteoPalabras('a la una a comer') == {'a': 2, 'la': 1, 'una': 1, 'comer': 1})
print('Prueba 6.2:', parcial_1.conteoPalabras('b b aa aa aa') == {'aa': 3, 'b': 2})
print('Prueba 6.3:', parcial_1.conteoPalabras('a') == {'a': 1})

print('Prueba 8.1:', parcial_1.modificarTupla((1, 2, 3), 0, True) == (True, 2, 3))
print('Prueba 8.2:', parcial_1.modificarTupla(1234, 0, 'True') is None)
print('Prueba 8.3:', parcial_1.modificarTupla([], 0, 'True') is None)
print('Prueba 8.4:', parcial_1.modificarTupla((1, 2, 3), 100, 'True') is None)

print('Prueba 9.1', parcial_1.transformarMedida({'c': 100}) == {'F': 212.0})
print('Prueba 9.2', parcial_1.transformarMedida({'f': 32}) == {'C': 0.0})

print('Prueba 10.1', parcial_1.obtenerBilletes(123) == {100: 1, 20: 1, 2: 1, 1: 1})
print('Prueba 10.2', parcial_1.obtenerBilletes(14) == {2: 2, 10: 1})