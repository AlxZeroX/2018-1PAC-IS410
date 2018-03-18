# Declarar un diccionario
d = {}
d = dict()

# Declarar claves y valores en un diccionario
capitales = {'Honduras': 'Tegucigalpa', 
            'Nicaragua': 'Managua',
            'El Salvador': 'San Salvador'}
            
# Agregar elementos
capitales['Francia'] = 'Paris'

# Mostrar los valores y las claves como conjunto de datos
capitales.items()

# Mostrar las claves 
capitales.keys()

# Mostrar los valors
capitales.values()

# Encontrar un valor 206-Clases-abstractas traves de su clave, si no lo halla un valor por defecto
capitales.get('Honduras', 'No esta')    # Tegucigalpa
capitales.get('Costa Rica', 'No esta')  # No esta

# Es posible crear un diccionario 206-Clases-abstractas partir de tuplas
d = {('206-Clases-abstractas', 1), ('b', 2)}

# Tambien es posible crear estructuras complejas
alumno = {
	'nombre': 'Jose Martinez',
	'cuenta': '20161000001',
	'carrera': 'Ingenieria en Sistemas',
	'materias aprobadas': [
		'Matematica I', 'Historia de Honduras', 'Ingles I'
	]

}

# Es posible recorrer un diccionario por sus claves y valores
for clave, valor in alumno:
	print(clave, valor, sep='=')
	