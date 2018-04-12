class Test:
    def __new__(cls, *args, **kwargs):
        print('Ejecucion __new__')

        # Se retorna el objeto creado
        return super().__new__(cls, *args, *kwargs)



    def __init__(self):
        print('Ejecucion de __init__')

if __name__ == '__main__':
    objeto = Test()
