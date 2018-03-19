[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)
# Encapsulamiento

### Ocultamiento de datos
En la mayoría de lenguajes de programación orientado a objetos se tiene diversos tipos de ocultamiento de datos, siendo 
los más comúnes:
- **Público:** Acceso y modificación de atributos y métodos fuera del objeto.
- **Privado:** Los atributos y métodos del objeto solo puede ser accedido y modificado dentro del objeto.
- **Protegido:** Atributo y métodos del objeto solo son accedidos por él mismo y objetos de clases derivadas.

En el caso de Python, los atributos y métodos de objeto son accedidos de forma público. No existe ocultamiento privado 
o protegidos.

Sin embargo, Python permite ocultar atributos para evitar el acceso directo de los mismos. 
Utilizando doble guión bajo (__) se puede establecer que un atributo se oculte. Aunque, es posible acceder con la 
notación: ```objeto._NombreClase__AtributoOculto```

```Python

class Contador:
    def __init__(self):
        # Atributo oculto
        self.__conteo = 0

    def contar(self):
        print (self.__conteo)

c1 = Contador()
# No pudo acceder al atributo oculto
c1.__conteo = 1000
# Imprime 0
c1.contar()

# Si pudo acceder al atributo oculto
c1._Contador__conteo = 1000
# Imprime 1000
c1.contar()
```

### Propiedades
Al utilizar atributos ocultos es posible utilizar los métodos de acceso (getters) y de modificación (setters), tal como 
se realiza en JAVA. Además, es posible utilizar las propiedades, las cuales permiten que funciones de acceso y 
modificación se comporten como un atributo público.

```python
class Vaso:
    def __init__(self, capacidad):
        self.__contenido = 0
        self.capacidad= capacidad

    @property
    def contenido(self):
        return self.__contenido

    @contenido.setter
    def contenido(self, valor):
        if (valor > self.capacidad):
            self.__contenido = self.capacidad
        else:
            self.__contenido = valor


if __name__ == '__main__':
    vaso1 = Vaso(10)
    # Llamando a la función setter
    vaso1.contenido = 8
    # Llamando a la función getter
    print(vaso1.contenido)
    
```

Existe otra forma de crear propiedades. En este caso, utilizando de forma explícita las funciones getter y setter.
```python
class Vaso:
    def __init__(self, capacidad):
        self.__contenido = 0
        self.capacidad= capacidad

    def get_contenido(self):
        return self.__contenido

    def set_contenido(self, valor):
        if (valor > self.capacidad):
            self.__contenido = self.capacidad
        else:
            self.__contenido = valor

    contenido = property(get_contenido, set_contenido)
    
    
if __name__ == '__main__':
    vaso1 = Vaso(10)
    # Llamando a la función setter
    vaso1.contenido = 8
    # Llamando a la función getter
    print(vaso1.contenido)
    
```

#### Fuentes:
- https://docs.python.org/3.5/library/functions.html?highlight=property#property
- https://www.programiz.com/python-programming/property
- https://www.python-course.eu/python3_properties.php