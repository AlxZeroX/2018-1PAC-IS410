# módulo de números Fibonacci

# escribe la serie Fibonacci hasta n
def print_fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


# devuelve la serie Fibonacci hasta n
def list_fibonacci(n):
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado


# se puede utilizar el modulo como si fuese un script
if __name__ == '__main__':
    import sys

    numero = int(sys.argv[1])
    print_fibonacci(numero)
