# Areli Sarai García Medina | 203010380
# Práctica 47 - Expresiones regulares - findall() - RegEx

import re

texto1 = "Areli Sarai García Medina"

busqueda1 = re.search("A", texto1)
busqueda2 = re.findall("a", texto1)
busqueda3 = re.search("o", texto1)
busqueda4 = re.findall("e", texto1)
busqueda5 = re.search("Areli García", texto1)

print(busqueda1)
print(busqueda2)
print(busqueda3)
print(busqueda4)
print(busqueda5)