# Areli Sarai García Medina | 203010380
# Práctica 49 - Secuencias especiales, metacaracteres y sets - Expresiones regulares - RegEx

import re

texto1 = "Areli Sarai García Medina - 20310380 - Ingeniería Mecatrónica"

resultado = re.findall("A...i|García|20310380", texto1)
print(resultado)

resultado2 = re.findall("\D", texto1)
print(resultado2)

resultaddo3 = re.findall("[a-gA-G]", texto1)
print(resultaddo3)

resultado4 = re.findall("[^aeiíó]", texto1)
print(resultado4)