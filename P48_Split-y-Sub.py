# Areli Sarai García Medina | 203010380
# Práctica 48 - Expresiones regulares - split() y sub() - RegEx

# Se importa la librería 're' para las operaciones de coincidencia de expresiones regulares
import re

# Se declara el 'texto1' como string
texto1 = "Areli Sarai García Medina - 20310380 - Ingeniería Mecatrónica"

# Se separará cada espacio ' ' del texto
resultado = re.split(" ", texto1)
print(resultado)

# Se separará cada espacio ' ' del texto, limitándolo a las primeras 5 coincidencias
resultado2 = re.split(" ", texto1, 5)
print(resultado2)

print("\n\n")

# Se sustituirá cada espacio ' ' por '/' en el texto
resultado3 = re.sub(" ", "/", texto1)
print(resultado3)

# Se sustituirá cada espacio ' ' por '/' en el texto, limitándolo a las primeras 6 coincidencias
resultado4 = re.sub(" ", "/", texto1, 6)
print(resultado4)