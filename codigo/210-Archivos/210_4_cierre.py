# Intentara abrir y cerrar el archivo 10,000 veces

def abrir_archivo(n):
    files = []

    for x in range(n):
        f = open('foo.txt', 'w')
        files.append(f)


def abrir_cerrar_archivo(n):
    files = []

    for x in range(n):
        f = open('foo.txt', 'w')
        f.close()
        files.append(f)


# Intentar abrir el archivo (OSError)
#abrir_archivo(10000)

# Abrir y cerrar el archivo
abrir_cerrar_archivo(10000)