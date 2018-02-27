[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)
# Manejo de Excepciones
## Definición
Los errores de programación se presentan cuando un programa finaliza con un resultado indeseado. Estos pueden ser:
- Errores de sintaxis
- Excepciones

Por lo general, las excepciones ocurren bajo ciertas condiciones, como ser: una división entre cero, un ciclo infinito, una variable no inicializada, acceso a un índice en una colección no definido, al fallar un intento de conversión de tipos, etc.

Las excepciones son eventos relacionados directamente con la ejecución de un programa. En general, cuando ocurre una excepción el sistema operativo aborta el programa.

## Manejo
Para evitar que el programa sea abortado es necesario poder controlar las excepciones. Para ello Python provee el uso de las palabras clave **try** / **except**

```python
try:
    #Bloque que debe probarse si tiene excepciones
except TipoError:
    #Bloque que se ejecuta en caso de una excepción
```

Es posible y aconsejable que después del bloque **try** existan diversos bloques **except** para definir la excepción exacta que se está manejando. 

```python
try:
    #Bloque que debe probarse si tiene excepciones
except TipoError1:
    #Bloque que se ejecuta en caso de una excepción
except TipoError2:
    #Bloque que se ejecuta en caso de otro tipo de excepción
```

También es necesario que al final exista un bloque except sin ningún tipo. Esto debido a que pueden existir excepciones no controladas.

```python
try:
    #Bloque que debe probarse si tiene excepciones
except TipoError1:
    #Bloque que se ejecuta en caso de una excepción
except TipoError2:
    #Bloque que se ejecuta en caso de otro tipo de excepción
except:
    #Bloque final de excepción
```

Finalmente, se puede agregar un bloque **else** al final para indicar que código se ejecutará en caso de que el bloque try no tenga errores.

```python
try:
    #Bloque que debe probarse si tiene excepciones
except TipoError1:
    #Bloque que se ejecuta en caso de una excepción
except TipoError2:
    #Bloque que se ejecuta en caso de otro tipo de excepción
except:
    #Bloque final de excepción
else:
    #Bloque que se ejecuta si el try no tiene excepciones
```

### Lanzando excepciones
La declaración **raise** permite al programador forzar a que ocurra una excepción específica. Por ejemplo:

```python
raise NameError('Hola')
```

Se puede utilizar un llamado sin necesidad de mensaje.

```python
raise ValueError
```

Es posible relanzar la excepción para que en otra parte pueda ser manejada.

```python
try:
    raise NameError('Hola')
except NameError:
    print('Ocurrrio una excepcion')
    raise
```

### Bloque Finally
Existe una clausula opcional denominada **finally** la cual, si se utiliza, se llama ocurra o no una excepción. En aplicaciones reales, la cláusula **finally** es útil para liberar recursos externos (como archivos o conexiones de red), sin importar si el uso del recurso fue exitoso.

## Excepciones comunes
A continuación se muestra un listado de las excepciones más comunes:[[2]](https://code.tutsplus.com/es/tutorials/how-to-handle-exceptions-in-python--cms-28621) 
- **NameError:** Esta excepción es levantada cuando el programa no puede encontrar un nombre local o global. El nombre que podría no ser encontrado está incluido en el mensaje de error.
- **TypeError:** Esta excepción es levantada cuando una función se le pasa un objeto del tipo inapropiado como su argumento. Más detalles sobre el tipo incorrecto son proporcionados en el mensaje de error.
- **ValueError:** Esta excepción ocurre cuando un argumento de función tiene el tipo correcto pero un valor inapropiado.
- **NotImplementedError:** Esta excepción es levantada cuando se supone que un objeto apoye una operación pero no ha sido implementado aún. No deberías usar este error cuando la función dada no deba apoyar al tipo de argumento de entrada. En esas situaciones, levantar una excepción TypeError es más apropiado.
- **ZeroDivisionError:** Esta excepción es levantada cuando proporcionas el segundo argumento para una operación de división o módulo como cero.
- **FileNotFoundError:** Esta excepción es levantada cuando el archivo o diccionario que el programa solicitó no existe.

Existe un listado más detallado [a continuación](https://docs.python.org/3/library/exceptions.html#concrete-exceptions).


---

#### Fuentes
1. http://computacion.cs.cinvestav.mx/~ameneses/pub/tesis/ltesis/node15.html
2. https://code.tutsplus.com/es/tutorials/how-to-handle-exceptions-in-python--cms-28621
3. http://docs.python.org.ar/tutorial/3/errors.html
