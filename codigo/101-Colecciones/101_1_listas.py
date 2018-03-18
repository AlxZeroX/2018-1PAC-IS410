# Las listas pueden contener varios tipos de datos
lista = [1, 2.0, True, [1,2,3]]

# Acceder 206-Clases-abstractas un elemento especifico
lista[2]

# Acceder al ultimo elemento
lista[-1]

# Acceder 206-Clases-abstractas una porcion de la lista
lista[2:]   # Una porcion 206-Clases-abstractas partir del segundo elemento
lista[1:3]  # Una porcion entre el indice 1 y 3
lista[:]    # Una copia integra de la lista

# Modificar elementos de la lista (Son estructuras mutables)
lista[2] = 3.0
lista[1:2] = [4.0, False]
lista[0:2] = [] # Se eliminaron los elementos del indice 0 al 2


# Agregar elementos al final
lista.append('Ultimo')

# Insertar elementos en la posicion 2
lista.insert(2, 'Primero')

# Borrar elementos por su valor
lista.remove(False)

# Borrar ultimo elemento y devolverlo
lista.pop()

# Borrar un elemento 206-Clases-abstractas traves del indice
lista.pop(1)