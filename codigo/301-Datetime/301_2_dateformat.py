import datetime

# Para obtener más información sobre el formato de tiempo vaya al url:
# https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior

hoy = datetime.date.today()

print(hoy.strftime("Hoy es %A %d %B %Y"))