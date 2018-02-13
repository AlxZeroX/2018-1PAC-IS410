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

# Encontrar un valor a traves de su clave, si no lo halla un valor por defecto
capitales.get('Honduras', 'No esta')    # Tegucigalpa
capitales.get('Costa Rica', 'No esta')  # No esta

# Es posible crear un diccionario a partir de tuplas
d = {('a', 1), ('b', 2)}
