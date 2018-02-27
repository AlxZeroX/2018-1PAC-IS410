entrada1 = input('Coloque primer numero: ')
entrada2 = input('Coloque segundo numero: ')

try:
    numero1 = int(entrada1)
    numero2 = int(entrada2)

    valor_division = numero1 / numero2
    
except Exception as ex:
    print('Error:', ex)    
else:
    print('Resultado de division: ', valor_division)

print ('Fin del programa'.center(80, '='))
