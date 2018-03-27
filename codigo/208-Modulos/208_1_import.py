import modulo
import modulo_con_nombre_largo as m_largo
import modulo.lista

# Todos los elementos son llamados a traves del modulo
print(modulo.lista)

# Tambien es posible acceder a funciones
print(modulo.sumar(1, 2))

# Y por ultimo, es posible crear objetos
test = modulo.Test()
test.mostrar()

print(m_largo.cadena)
