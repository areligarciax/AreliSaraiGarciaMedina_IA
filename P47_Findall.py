# Areli Sarai García Medina | 203010380
# Práctica 47 - Expresiones regulares - findall() - RegEx

# Se importa la librería 're' para las operaciones de coincidencia de expresiones regulares
import re

# Se declara el 'texto1' como string
texto1 = "Areli Sarai García Medina"

# Se busca la posición de la primera letra 'A'
busqueda1 = re.search("A", texto1)
# Se buscan todas las coincidencias de la letra 'a' en el texto
busqueda2 = re.findall("a", texto1)
# Se busca la posición de la primera letra 'o'
busqueda3 = re.search("o", texto1)
# Se buscan todas las coincidencias de la letra 'e' en el texto
busqueda4 = re.findall("e", texto1)
# Se busca la posición de la primera coincidencia de 'Areli García'
busqueda5 = re.search("Areli García", texto1)

# Se imprimen las posiciones y coincidencias
print(busqueda1)
print(busqueda2)
print(busqueda3)
print(busqueda4)
print(busqueda5)