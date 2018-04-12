class Test:
    def __new__(cls, *args):
        #if args[0] is False:
            #raise ValueError()
        if args[0] is True:
            return super().__new__(cls)

    def __init__(self, x):
        self.x = x
        print('Se llamo al __init__')


if __name__ == '__main__':
    s = Test(True)
    t = Test(False)

    print(type(s))
    print(type(t))