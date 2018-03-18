# Establecer un set
s1 = set([1, 2, 3, 4, 5])
s2 = set((3, 4, 5, 6, 7))

# Es posible utilizar esta notacion para un set
s3 = {0, 0, 1}		
# Para el caso anterior, solo hay dos elemento pues los set no permiten 
# elementos repetidos

# No soporta la indexacion
s1[0]

# Para agregar un elemento
s3.add(2)

# Para agregar varios elementos (el argumento es una coleccion)
s3.update([3, 4, 5])

# Para eliminar elementos se puede utilizar discard() o remove()
# La diferencia consiste en que si no se encuentra el elemento 206-Clases-abstractas borrar
# remove() genera un error
s3.discard(5)
s3.remove(4)

# Union de conjuntos
s1 | s2
s1.union(s2)

# Interseccion entre conjuntos
s1 & s2
s1.intersection(s2)

# Diferencia entre conjuntos
s1 - s2
s1.difference(s2)

# Diferencia simetrica
s1 ^ s2
s1.symmetric_difference(s2)

# Determinar subconjuntos
s3 = set((1, 2))

s3.issubset(s1)     # True