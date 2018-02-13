# Establecer un set
s1 = set([1, 2, 3, 4, 5])
s2 = set((3, 4, 5, 6, 7))

# No soporta la indexacion
s1[0]

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