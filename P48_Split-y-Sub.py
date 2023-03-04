# Areli Sarai García Medina | 203010380
# Práctica 48 - Expresiones regulares - split() y sub() - RegEx

import re

texto1 = "Areli Sarai García Medina - 20310380 - Ingeniería Mecatrónica"

resultado = re.split(" ", texto1)
print(resultado)

resultado2 = re.split(" ", texto1, 5)
print(resultado2)

print("\n\n")

resultado3 = re.sub(" ", "/", texto1)
print(resultado3)

resultado4 = re.sub(" ", "/", texto1, 5)
print(resultado4)