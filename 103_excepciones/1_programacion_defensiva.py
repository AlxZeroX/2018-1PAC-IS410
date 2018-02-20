entrada1 = input('Coloque primer numero: ')
entrada2 = input('Coloque segundo numero: ')

if entrada1.isdigit() and entrada2.isdigit():
    numero1 = int(entrada1)
    numero2 = int(entrada2)

    if numero2 != 0:
        valor_division = numero1 / numero2
        print('Resultado de division: ', valor_division)
    else:
        print('Intento dividir entre cero')
else:
    print('Intento convertir cadenas no numericas')

print ('Fin del programa'.center(80, '='))
