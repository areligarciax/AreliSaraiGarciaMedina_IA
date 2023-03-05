# Areli Sarai García Medina | 203010380
# Práctica 49 - Secuencias especiales, metacaracteres y sets - Expresiones regulares - RegEx


# Se importa la librería 're' para las operaciones de coincidencia de expresiones regulares
import re

# Se declara el 'texto1' como string
texto1 = "Areli Sarai García Medina - 20310380 - Ingeniería Mecatrónica"

# Se busca en el texto las coincidencias siguientes
# El operador '|' es como decir 'y'
resultado = re.findall("A...i|García|20310380", texto1)
print(resultado)

# El operador '/D' devuelve una coincidencia si en el string no hay ningún dígito.
resultado2 = re.findall("\D", texto1)
print(resultado2)

# Devuelve todas las letras de la a a la g en minúsculas y de la A a la G en mayúsculas
resultaddo3 = re.findall("[a-gA-G]", texto1)
print(resultaddo3)

# Buscará cualquier carácter excepto a, e, i, í y ó, es decir, las vocales con o sin tilde.
resultado4 = re.findall("[^aeiouáéíóú]", texto1)
print(resultado4)