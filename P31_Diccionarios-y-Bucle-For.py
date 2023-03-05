# Areli Sarai García Medina | 203010380
# Práctica 31 - Como usar diccionarios con el bucle For


# Se crean los diccionarios con sus elementos y atributos

alumno1 = {
    "Nombre": "Sofía Veazey",
    "Registro": "20310136",
    "Edad": "21",
    "Nacionalidad": "Canadiense"
}

alumno2 = {
    "Nombre": "Areli García",
    "Registro": "20310380",
    "Edad": "20",
    "Nacionalidad": "Mexicana"
}

alumno3 = {
    "Nombre": "Josué Medina",
    "Registro": "20310037",
    "Edad": "25",
    "Nacionalidad": "Mexicana"
}

alumno4 = {
    "Nombre": "Cecille Bechelani",
    "Registro": "20310279",
    "Edad": "20",
    "Nacionalidad": "Italiana"
}

# Se imprimen los elementos de los diccionarios con ayuda del ciclo for
# 'x' para el string de los atributos y 'y' para lo que contiene

for x, y in alumno1.items():
    print(x, ": ", y)

print("\n")

for x, y in alumno2.items():
    print(x, ": ", y)

print("\n")

for x, y in alumno3.items():
    print(x, ": ", y)

print("\n")

for x, y in alumno4.items():
    print(x, ": ", y)

print("\n")