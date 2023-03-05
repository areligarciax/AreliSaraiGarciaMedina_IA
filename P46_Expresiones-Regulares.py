# Areli Sarai García Medina | 203010380
# Práctica 46 - Expresiones regulares - search() - RegEx

# Se importa la librería 're' para las operaciones de coincidencia de expresiones regulares
import re

# Se declara el 'texto1' como string
texto1 = "Areli Sarai García Medina"

# Se busca la posición de la primera letra 'A'
busqueda1 = re.search("A", texto1)
# Se busca la posición de la primera letra 'a'
busqueda2 = re.search("a", texto1)
# Se busca la posición de la primera letra 'o'
busqueda3 = re.search("o", texto1)
# Se busca la posición de la primera letra 'e'
busqueda4 = re.search("e", texto1)
# Se busca la posición de la primera coincidencia de 'Areli García'
busqueda5 = re.search("Areli García", texto1)


# Se imprimen las posiciónes encontradas
print(busqueda1)
print(busqueda2)
print(busqueda3)
print(busqueda4)
print(busqueda5)