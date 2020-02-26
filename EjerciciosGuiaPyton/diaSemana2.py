from datetime import datetime, date, time, timedelta
import calendar
dias=["domingo","lunes"," martes","miercoles","jueves","viernes","sabado"]
formato = "%d/%m/%Y"
fecha = input('ingrese una  fecha (dd/mm/aaaa): ')
objeto_datetime = datetime.strptime(fecha, formato)
d = datetime.isoweekday(objeto_datetime)
print(dias[d])
