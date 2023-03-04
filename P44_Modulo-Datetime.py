# Areli Sarai García Medina | 203010380
# Práctica 44 - Trabajar con fechas con el módulo datetime

import datetime

fechahoy = datetime.datetime.now()

print("La fecha del día de hoy es -> ", fechahoy)
print("\n\n\t\t- C U M P L E A Ñ O S -")

persona1 = datetime.datetime(2002, 6, 13)
persona2 = datetime.datetime(2002, 9, 27)
persona3 = datetime.datetime(1967, 1, 8)
persona4 = datetime.datetime(1994, 7, 3)
persona5 = datetime.datetime(2002, 8, 23)

print("\n\t -> Areli\nDía:", persona1.day, "\nMes:", persona1.month, "\nAño:", persona1.year)
print("\n\t -> Cecille\nDía:", persona2.day, "\nMes:", persona2.month, "\nAño:", persona2.year)
print("\n\t -> Sonia\nDía:", persona3.day, "\nMes:", persona3.month, "\nAño:", persona3.year)
print("\n\t -> Josué\nDía:", persona4.day, "\nMes:", persona4.month, "\nAño:", persona4.year)
print("\n\t -> Arlet\nDía:", persona5.day, "\nMes:", persona5.month, "\nAño:", persona5.year)


