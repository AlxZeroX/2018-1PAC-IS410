import datetime

# Dia actual
hoy = datetime.date.today()
print('today():', hoy)

# Es posible dividir una expresion 
print('Año:', hoy.year)
print('Mes:', hoy.month)
print('Dia:', hoy.day)

# Algunas funciones
print('Dia de la semana(0 es lunes):', hoy.weekday())
print('Dia de la semana(0 es domingo):', hoy.isoweekday())
print('Calendario(Año, numero de semana, dia de la semana):', hoy.isocalendar())
print('Representacion ISO-8601 de la fecha (YYYY-MM-DD):', hoy.isoformat())

# Es posible crear nuestras propias fechas
dia_independencia = datetime.date(2018, 9, 15)
print('Dia de independencia:', dia_independencia)

navidad = datetime.date(day=25, year=hoy.year, month=12)
print('Navidad:', navidad)

try:
    dia_error = datetime.date(2018, 2, 31)
except Exception as ex:
    print(ex)
