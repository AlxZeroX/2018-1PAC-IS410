[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)
# Polimorfismo

## Definición
Es la cualidad de ser capaz de asumir diferentes formas. En orientación a objetos, es la habilidad de vincular objetos de diferentes tipos a un solo identificador en tiempo de ejecución.

Se refiere a la capacidad de acceder a múltiples funciones a través del mismo interfaz. Es decir que un mismo identificador, o función puede tener diferentes comportamientos con respecto al contexto en el que sea ejecutado.[[1]](http://www.codigo-facil.com/es/poo-php-polimorfismo.php
)

## Tipos
- Sobrecarga
- Paramétrico
- Subtipado

### Polimorfismo de Sobrecarga
El polimorfismo de sobrecarga ocurre cuando las funciones del mismo nombre existen, con funcionalidad similar, en clases que son completamente independientes una de otra (éstas no tienen que ser clases secundarias de la clase objeto).

El polimorfismo de sobrecarga, también nos permite definir operadores cuyos comportamientos varían de acuerdo a los parámetros que se les aplican.

**Ejemplo**
```bash
3 + 2 (Denota una suma aritmética)

“hola” + “mundo” (Denota una concatenación de String)
```
### Polimorfismo Paramétrico
El polimorfismo paramétrico es la capacidad para definir varias funciones utilizando el mismo nombre, pero usando parámetros diferentes (nombre y/o tipo). El polimorfismo paramétrico selecciona automáticamente el método correcto a aplicar en función del tipo de datos pasados en el parámetro.

**Ejemplo**

```java
int suma(int a, int b)
int suma(int a, int b, int c)
float suma (float a, float b)
```

### Polimorfismo de subtipado
La habilidad para redefinir un método en clases que se hereda de una clase base se llama especialización. 

Por lo tanto, se puede llamar un método de objeto sin tener que conocer su tipo intrínseco: esto es polimorfismo de subtipado. 

Permite no tomar en cuenta detalles de las clases especializadas de una familia de objetos, enmascarándolos con una interfaz común (siendo esta la clase básica).

**Ejemplo**

Imagine un juego de ajedrez con las clases rey, reina, alfil, caballo, torre y peón, cada uno heredando de la clase pieza.

El método `movimiento()` podría, usando polimorfismo de subtipado, hacer el movimiento correspondiente de acuerdo a la clase objeto que se llama. Esto permite al programa realizar el movimiento de pieza sin tener que verse conectado con cada tipo de pieza en particular.

```java
abstract class Pieza {
    abstract public void mover();
}

class Reyna extends Pieza {
    public void mover() {
        System.out.println("En todas direcciones sin restricciones");
    }
}

class Rey extends Pieza {
    public void mover() {
        System.out.println("En todas direcciones, un cuadro a la vez");
    }
}

class Torre extends Pieza {
    public void mover() {
        System.out.println("Vertical y horizontal");
    }
}

public class ProbarPieza {
    public static void main(String[] args) {
        Pieza reyna = new Reyna();
        Pieza rey = new Rey();
        Pieza torre1 = new Torre();
        
        movimiento(reyna);
        movimiento(rey);
        movimiento(torre1);
    }

    public static void movimiento(Pieza p) {
        p.mover();
    }
}
```

## Polimorfismo en Python
Dado que Python es un lenguaje de tipado dinámico, posee características diferentes en cuanto al aprovechamiento del polimorfismo.

### Duck Typing
`Si camina como pato, nada como pato y suena como pato, probablemente es un pato`. En lenguajes dinámicos como Python no es necesaria la herencia para tener polimorfismo, tan solo es necesario que objetos se comporten de manera similar.

```python
class Pato:
    def graznar(self):
        print('Cuac!')
        
class FalsoPato:
    def graznar(self):
        print('Cuac! (falso)')
    
# Funcion probar metodos similares en
# objetos que no tienen relacion de herencia
def hacer_graznar(objeto):
    objeto.graznar()
    
pato1 = Pato()
hacer_graznar(pato1)

pato2 = FalsoPato()
hacer_graznar(pato2)
```

### Sobrecarga de operadores
Parte de la funcionalidad de Python consiste en utilizar los operadores, tanto aritmeticos como logicos, para nuevas labores a partir de ciertos métodos. 

Por ejemplo, es posible utilizar el operador (+) para sumar o concatenar objetos:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        sumax = self.x + other.x
        sumay = self.y + other.y
        vector_suma = Vector(sumax, sumay)
        return vector_suma

    def __sub__(self, other):
        restax = self.x - other.x
        restay = self.y - other.y
        vector_resta = Vector(restax, restay)
        return vector_resta

v1 = Vector(1, 2)
v2 = Vector(2, 3)

v3 = v1 + v2
v4 = v2 - v1
```
Además es posible utilizar otros operadores matemáticos y lógicos para su incorporación en nuevas estructuras.

---
[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)
