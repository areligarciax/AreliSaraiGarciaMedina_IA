# Areli Sarai García Medina | 203010380
# Práctica 45 - Trabajar con fechas con el método strftime()

# Se importan las librerías 'datetime' y 'locale'
import datetime, locale

# Con esta línea se traduce la información a idioma español
locale.setlocale(locale.LC_ALL, "es-Es")

# Se le asigna a 'persona1' la fecha y hora específica
persona1 = datetime.datetime(2002,6,13,9,12)

# Con ayuda de 'strftime' se formatean las fechas en strings determinado por el formato de parámetro

#Día de la semana abreviado
print(persona1.strftime("Día de la semana abreviado: %a "))
# Día de la semana completo
print(persona1.strftime("Día de la semana completo: %A "))
# Mes abreviado
print(persona1.strftime("Mes abreviado: %b "))
#Mes completo
print(persona1.strftime("Mes completo: %B "))
# Fecha completa
print(persona1.strftime("Fecha completa: %c "))
# Siglo (empieza a contar desde cero)
print(persona1.strftime("Siglo (empieza a contar desde cero): %C "))
# Día del mes (01 - 31) (agrega 0)
print(persona1.strftime("Día del mes (01 - 31): %d "))
# Día/hora/año
print(persona1.strftime("Día/hora/año: %D "))
# Día del mes (1 - 31)
print(persona1.strftime("Día del mes (1 - 31): %e "))
# Año en dos dígitos
print(persona1.strftime("Año en dos dígitos: %g "))
# Año en cuatro dígitos
print(persona1.strftime("Año en cuatro dígitos: %G "))
# Mes abreviado
print(persona1.strftime("Mes abreviado: %h "))
# Hora en formato de 24 horas
print(persona1.strftime("Hora (00 - 23): %H "))
# Hora en formato de 12 horas
print(persona1.strftime("Hora (01 - 12): %I "))
# Día del año
print(persona1.strftime("Día del año: %j "))
# Mes del 01 al 12
print(persona1.strftime("Mes del 01 al 12: %m "))
# Minuto
print(persona1.strftime("Minuto: %M "))
# Hora y minutos
print(persona1.strftime("Hora y minutos: %R"))
# Segundos
print(persona1.strftime("Segundos: %S"))
# Hora, minutos y segundos
print(persona1.strftime("Hora, minutos y segundos: %T"))
# Día de la semana (número)
print(persona1.strftime("Día de la semana (número): %u"))
# Semana del año (empieza en domingo)
print(persona1.strftime("Semana del año (empieza en domingo): %U"))
# Semana del año (empieza en lunes)
print(persona1.strftime("Semana del año (empieza en lunes): %W"))
# Día de la semana (empieza en domingo)
print(persona1.strftime("Día de la semana (empieza en domingo): %w"))
# Día/mes/año de dos dígitos
print(persona1.strftime("Día/mes/año de dos dígitos: %x"))
# Hora/minutos/segundos
print(persona1.strftime("Hora/minutos/segundos: %X"))
# Año corto
print(persona1.strftime("Año corto: %y"))
# Año largo
print(persona1.strftime("Año largo: %Y"))