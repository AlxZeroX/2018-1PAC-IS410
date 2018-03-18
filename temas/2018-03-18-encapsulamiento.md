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
