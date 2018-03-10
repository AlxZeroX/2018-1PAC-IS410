str1 = 'Hola'
str2 = 'Mundo'

# Es posible concatenar 2 cadenas
str1 + str2

# Por otro lado 2 cadenas cercanas, aun con espacio de por medio se define como
# concatenacion
print('Hola' 'mundo')

# Es posible repetir cadenas
str1_repetida = str1 * 4

# Convertir a mayusculas
str1.upper()

# Convertir a minuscula
str1.lower()

# Convertir a formato titulo
str1.title()

# Crear un texto centrado, se puede alinear tambien con ljust y rjust
str1.center(80, '=')

# Rellenar cadena con ceros
str3 = "120"
str3.zfill(10)

# Reemplazar una cadena
"Hola nombre, apellido".replace("nombre", "Ana").replace("apellido", "Lopez")

# Eliminar caracteres
str4 = "   hola   "
str4.lstrip()	# Izquierda
str4.rstrip()	# Derecha
str4.strip()	# Ambos lados

# Juntar elementos en una cadena
str5 = "estan"
lista = ["Hola", "que", "tal"]
str5.join(lista)

# Separa cadena en elementos
str6 = "Hola que tal estan"
lista1 = str6.split()


