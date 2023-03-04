# Areli Sarai García Medina | 203010380
# Práctica 46 - Expresiones regulares - search() - RegEx

import re

texto1 = "Areli García"

busqueda1 = re.search("A", texto1)
busqueda2 = re.search("a", texto1)
busqueda3 = re.search("o", texto1)
busqueda4 = re.search("e", texto1)
busqueda5 = re.search("Areli García", texto1)

print(busqueda1)
print(busqueda2)
print(busqueda3)
print(busqueda4)
print(busqueda5)