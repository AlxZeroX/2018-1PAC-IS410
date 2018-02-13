# Definir una tupla de un elemento
t1 = (1,)

# Definir una tupla de mas de un elemento
t2 = (1,2, 3, 3)

# Otra definicion de tupla
t3 = 4, 5, 6

# Definir una tupla utilizando un objeto iterador y la funcion tuple
t3 = tuple(range(11))

# Tratar de modificar un elemento de la tupla
t1[0] = 0       # Se genera un TypeError

# No es posible utilizar metodos para modificar la tupla solamente los de 
# lectura de elementos
t2.count(3)     # Debe retornar 2
