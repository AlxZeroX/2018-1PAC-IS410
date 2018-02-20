entrada = input('Coloque el monto que desea retirar: ')

try:
    saldo = 2500
    monto = float(entrada)

    if (saldo < monto):
        raise Exception('Fondos insuficientes')
    else:
        saldo -= monto
        print('Queda en la cuenta:', saldo)

except ValueError:
    print('No ha colocado un monto')
except Exception as ex:
    print('Error:', ex)

print ('Fin del programa'.center(80, '='))
    