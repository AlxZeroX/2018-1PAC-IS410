'''
1. Crear un programa que encuentre la palabra con mayor cantidad de caracteres en una lista. En caso de tener dos
palabras con la misma cantidad, establezca por el orden alfabético. En caso de excepción o no encontrar nada, retornar
una cadena vacia.

def hallarPalabraMayor(lista: list) -> str:
'''
def hallarPalabraMayor(lista: list) -> str:
    mayor_tamaño = 0
    mayor = ''

    try:
        for elemento in lista:
            palabra = str(elemento)
            tamaño = len(palabra)

            if tamaño > mayor_tamaño or (tamaño == mayor_tamaño and palabra > mayor):
                mayor = palabra
                mayor_tamaño = tamaño
    except Exception as ex:
        print(ex)

    return mayor

'''
2. Encontrar la cantidad de números pares que pueden encontrarse en una lista. En caso de hallar una excepción o no 
encontrar nada, retornar cero. 

def hallarPares(lista: list) -> int: 
'''

def hallarPares(lista: list) -> int:
    cantidad_pares = 0

    try:
        for elemento in lista:
            numero = int(elemento)

            if numero % 2 == 0:
                cantidad_pares += 1
    except ValueError:
        pass

    return cantidad_pares

'''
3. Generar la secuencia de números armónicos. 
En caso de hallar un número 'n' mayor que cero, devolver una cadena de este tipo: Para n=3, retornar "1 + 1/2 + 1/3". 
En caso de que 'n' sea un número menor o igual a cero o sea flotante, debe generarse una excepción que indique que el 
argumento debe ser un entero positivo. 

def generarArmonicos(n: int) -> str: 
'''

# Puede utilizarse bytearray en lugar de concatenar cadenas
def generarArmonicos(n: int) -> str:
    esError = False

    if type(n) is not int:
        esError = True
    elif n <= 0:
        esError = True
    else:
        armonico = '1'

        if n > 1:
            for x in range(2, n + 1):
                armonico += ' + 1/{}'.format(x)
    if esError:
        raise Exception('n debe ser un numero entero mayor que cero')
    else:
        return armonico

'''
4. Determinar la posible edad de un persona 
a través de la cédula de identidad de la persona, asumiento que utiliza el formato hondureño (0000-0000-00000) 

def obtenerEdad(cedula: str) -> int: 
'''

def obtenerEdad(cedula: str) -> int:
    edad = 0

    try:
        partes = cedula.split('-')
        año = int(partes[1])
    except IndexError:
        print('Formato invalido')
    except Exception as ex:
        print(ex)
    else:
        # Ya que no se han visto el manejo de fechas, se dejar el valor del año actual
        edad = 2018 - año

    return edad

'''
5. Determinar el dígito más significativo de un número. Por ejemplo para n=123, el dígito más significativo es uno 

def obtenerDigitoMasSignificativo(n: int) -> int: 
'''

def obtenerDigitoMasSignificativo(n: int) -> int:
    cadena = str(n)
    numero = 0

    try:
        numero = int(cadena[0])
    except:
        pass

    return numero

'''
6. Crear un programa que determine de una cadena cada palabra que existiera en ella y que pudiera capturarse la palabra 
y el número de veces que esa palabra está en la cadena. Por ejemplo: 'Este es un dia para recordar o para olvidar'. 
Este = 1, es = 1, un = 1, dia = 1, para = 2, recordar = 1, o = 1, olvidar = 1. 

def conteoPalabras(cadena: str) -> ???? (que tipo de dato es el idóneo para esta tarea) 
'''

'''
La estructura más acorde para esta labor es un diccionario ya que permite almacenar, por cada elemento una clave y un
valor, de esta forma la clave es cada palabra única y el valor es el conteo de la misma.
'''
def conteoPalabras(cadena: str) -> dict:
    cadena = str(cadena)
    palabras = cadena.split()
    diccionario = dict()

    for palabra in palabras:
        # Determinar si ya existe la palabra en el diccionario
        if (palabra in diccionario.keys()):
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario
'''
7. Crear un programa tal que sea posible generar al menos 5 excepciones de la documentación de Python.
'''

# La respuesta es variable

'''
8. Crear un programa que permite modificar un elemento de una tupla. Si el índice no existe dentro de la tupla, generar
la excepción más idónea para ello. def modificarTupla(t: tuple, indice: int, valor: object) -> tuple: 
'''

# No es posible modificar una tupla pero es posible 'descongelarla' utilizando listas
def modificarTupla(t: tuple, indice: int, valor: object) -> tuple:
    tupla = None

    try:
        lista = list(t)
        lista[indice] = valor
    except Exception as ex:
        print(ex)
    else:
        tupla = tuple(lista)

    return tupla

'''
9. Definir un programa que transforme de grados Celsius a Fahrenheit, el diccionario tiene que tener como clave la 
unidad de temperatura (C o F) y como valor la propia temperatura, deben transformarse a la otra unidad y se retornar un 
diccionario con la nueva medida y el nuevo valor. def transformarMedida(d: dict) -> dict:
'''

def transformarMedida(d: dict) -> dict:
    if type(d) is not dict:
        raise Exception('Es necesario un diccionario')

    temperatura = 0
    clave = None

    if 'C' in d.keys():
        temperatura = d['C']
        clave = 'F'
    elif 'c' in d.keys():
        temperatura = d['c']
        clave = 'F'
    elif 'F' in d.keys():
        temperatura = d['F']
        clave = 'C'
    elif 'f' in d.keys():
        temperatura = d['f']
        clave = 'C'

    if clave == 'F':
        resultado = 9 * temperatura / 5 + 32
    elif clave == 'C':
        resultado = 5 * (temperatura - 32) / 9
    else:
        raise Exception('Clave incorrecta')

    return {clave: resultado}

'''
10. Definir un programa que permite definir mediante un diccionario los billetes en los cuales se puede descomponer 
un monto (la clave es el valor del billete y el valor la cantidad de los billetes). Se asume que la moneda es el lempira 
y que los montos son billetes de dicha denominación, por lo que el monto debe ser un valor entero. 
Ejemplo para un monto de 23 lempiras se tendría el siguiente diccionario {1: 1, 2: 1, 20: 1}

def obtenerBilletes(monto: int) -> dict: 
'''

def obtenerBilletes(monto: int) -> int:
    if type(monto) is not int:
        raise Exception('Monto debe ser un número entero')

    if monto <= 0:
        raise Exception('Monto debe ser un valor positivo')

    billetes = (500, 100, 50, 20, 10, 5, 2, 1)
    fajo = {}
    indice = 0

    while monto > 0:
        billete_actual = billetes[indice]

        if monto >= billete_actual:
            monto -= billete_actual
            fajo[billete_actual] = fajo.get(billete_actual, 0) + 1
        else:
            indice += 1

    return fajo

'''
*** Opcional *** 
Trate de crear una función que genere un número pseudo-aleatorio utilizando únicamente los elementos vistos hasta ahora 
en la clase.
'''