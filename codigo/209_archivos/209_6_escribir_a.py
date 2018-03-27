with open('conteo.txt', 'a') as fhandler:
    for x in range(10, 21):
        fhandler.write(str(x) + '\n')
