[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)
# Encapsulamiento
## Definición
Las variables del objeto se localizan en el centro o núcleo del objeto. Los métodos rodean y esconden el núcleo del objeto de otros objetos en el programa. Al empaquetamiento de las variables de un objeto con la protección de sus métodos se le llama encapsulamiento. Típicamente, el encapsulamiento es utilizado para esconder detalles de la puesta en práctica no importantes de otros objetos.[[1]](http://profesores.fi-b.unam.mx/carlos/java/java_basico3_3.html)

Es el proceso de almacenar en una misma sección los elementos de una abstracción que constituyen su estructura y su comportamiento; sirve para separar el interfaz contractual de una abstracción y su implantación.[[2]](https://styde.net/encapsulamiento-en-la-programacion-orientada-a-objetos/)

Existen dos productos que se forman a partir del encapsulamiento:
- Modularidad
- Ocultamiento de Datos

### Modularidad
- El código fuente de un objeto puede ser construido y mantenido, independientemente del código fuente de otros objetos. Así mismo, un objeto puede ser transferido alrededor del sistema sin alterar su estado y conducta.
- Las partes se denominan módulos.
- Cada módulo se puede reutilizar en más de un programa.
- Esto nos permite que los programas sean más fáciles de escribir y leer, de modificar y mantener.

### Ocultamiento de datos
Una forma de prevenir que se establezcan dependencias innecesarias entre partes de programas es usar mecanismos que permitan o ayuden al programador de un módulo impedir el establecimiento de dichas dependencias desde otros módulos. 

El ocultamiento de datos es la capacidad de algunos lenguajes de impedir que desde un módulo A se use una declaración incluidas en otro módulo B. Esto se hace limitando el ámbito de dicha declaraciones (se dice que la declaración no es visible desde A).

#### Ventajas del ocultamiento
- El ocultamiento de información ayuda a reducir la dependencias entre módulos, ya que, si se sabe que una declaración no es visible en otros módulos, podemos asumir que cualquier cambio que hagamos en la misma no afectará a esos otros módulos, sino únicamente a aquel módulo donde aparece.
- Este mecanismo permite al diseñador de un módulo seleccionar qué declaraciones del mismo serán visibles desde otros módulos, por tanto, se hace explícito en el programa las dependencias que se pueden establecer

#### Niveles de ocultamiento
En la mayoría de lenguajes de programación orientado a objetos se tiene diversos tipos de ocultamiento de datos, siendo 
los más comúnes:
- **Público:** Acceso y modificación de atributos y métodos fuera del objeto.
- **Privado:** Los atributos y métodos del objeto solo puede ser accedido y modificado dentro del objeto.
- **Protegido:** Atributo y métodos del objeto solo son accedidos por él mismo y objetos de clases derivadas.

En el caso de Python, los atributos y métodos de objeto son accedidos de forma pública. No existe ocultamiento privado 
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