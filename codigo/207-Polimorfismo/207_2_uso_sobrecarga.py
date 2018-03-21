import vector

def usar_suma(a, b):
    print(a + b)


usar_suma(1, 2)
usar_suma(3.0, 1.5)
usar_suma(True, False)
usar_suma('hola', 'mundo')
v1 = vector.Vector(1, 1)
v2 = vector.Vector(4, 5)
usar_suma(v1, v2)