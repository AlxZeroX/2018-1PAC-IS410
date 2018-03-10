# Con la funcion list se puede crear listas utilizan objetos iterables
listaA = list(range(11))
listaB = list('Hola')

# Uso de algunas funciones complementarias
numeros = [2, 43, 5, 12, 4]

# Obtener el numero de elementos de una lista
len(numeros)

# Valor maximo de una lista
max(numeros)

# Valor minimo de una lista
min(numeros)

# Suma de todos los valores de la lista (solo si es numero)
sum(numeros)

# Encontrar un valor dentro de una lista
43 in numeros   # Devuelve True

# Concatenar listas
listaC = listaA + listaB

# Repetir todos los elementos
listaD = listaB * 2