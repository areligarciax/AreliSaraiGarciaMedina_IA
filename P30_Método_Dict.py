# Areli Sarai García Medina | 203010380
# Práctica 30 - ¿Qué son los diccionarios de Python?

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

#nombres = alumno1["Nombre"], alumno2["Nombre"], alumno3["Nombre"], alumno4["Nombre"]
#print("Nombres:", nombres)

#reg = alumno1["Registro"], alumno2["Registro"], alumno3["Registro"], alumno4["Registro"]
#print("Registros:", reg)

#edad = alumno1["Edad"], alumno2["Edad"], alumno3["Edad"], alumno4["Edad"]
#print("Edades:", edad)

#nacionalidad = alumno1["Nacionalidad"], alumno2["Nacionalidad"], alumno3["Nacionalidad"], alumno4["Nacionalidad"]
#print("Nacionalidades:", nacionalidad)

muestraAlumno1 = dict(alumno1)
print("Datos del alumno 1:", muestraAlumno1)

muestraAlumno2 = dict(alumno2)
print("\nDatos del alumno 2:", muestraAlumno2)

muestraAlumno3 = dict(alumno3)
print("\nDatos del alumno 3:", muestraAlumno3)

muestraAlumno4 = dict(alumno4)
print("\nDatos del alumno 4:", muestraAlumno4)