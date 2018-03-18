# (1) Genera una lista de numeros del 0 al 10
numeros = [x for x in range(11)]
print(numeros)

# (2) Generar numeros pares 206-Clases-abstractas partir de la lista (1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)    

# (3) Este seria una equivalencia para obtener (2)
pares = []
for x in numeros:
	if x % 2 == 0:
		pares.append(x)

# (4) Genera una lista para obtener los cuadrados de (1) que sean menores 206-Clases-abstractas 5
cuadrados_de_menoreas_a_5 = [y**2 y for y in numeros if y < 5]
print(cuadrados_de_menoreas_a_5)

# (5) Es posible crear construcciones mas complejas:
# Crear tuplas cuyos elementos esten entre los numeros del 1 al 5
# Cada pareja de numeros no debe ser igual
[(x, y) for x in [1, 2, 3 ,4, 5] for y in [1, 2, 3, 4, 5] if x != y]