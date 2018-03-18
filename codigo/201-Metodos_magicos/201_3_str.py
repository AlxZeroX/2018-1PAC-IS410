
class Persona:
    # La funcion esta obligada 206-Clases-abstractas retornar un string
    def __str__(self):
        return 'Llamado del metodo __str__'

persona1 = Persona()

# Cuando al objeto se le pide que se comporte como una cadena (como cuando se utiliza la funcion print())
print(persona1)