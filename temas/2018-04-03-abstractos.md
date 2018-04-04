# Clases Abstractas

## Definición
- Las clases abstractas tienen como propósito establecer la herencia. Es así porque no pueden generar objetos propios.
- Pueden heredar métodos que no están implementados. Estos se denominan métodos abstractos.
- Los métodos abstractas deben ser implementados en la clase derivada. Siendo esta restricción de carácter obligatorio

## En Python
- Python no soporta de forma nativa las clases abstractas. Sin embargo, es posible implementarlas debido al módulo abc (Abstract Base Classes), utilizando metaclases y decoradores.
- Las metaclases son clases que instancian clases en lugar de objetos. Mientras que los decoradores agregan funcionalidad a las funciones mediante envoltorios (wrappers). 
- Para utilizar las clases abstractas debe importarse el modulo ABC. Luego, la clase abstracta debe heredar de la metaclase ABCMeta.

```python
import abc

class Figura2D(metaclass=abc.ABCMeta)
    def __init__(self, numero_lados, longitud):
        self.numero_lados = numero_lados
        self.longitud = longitud

    def calcular_perimetro(self):
        return self.longitud * self.numero_lados

    @abc.abstractclassmethod
    def calcular_area(self):
        '''Calcula el area de una figura regular'''
```