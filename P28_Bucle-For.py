# Areli Sarai García Medina | 203010380
# Práctica 28 - Bucle For

print("\t\t- B I E N V E N I D O -\n")

# Se crean las variables 'nombre', 'materia' y 'plantel' con entrada tipo string
# Se crean las variable 'registro' y 'calificacion' con entrada tipo entero

print("Ingresa tu nombre")
nombre = input()

print("\nIngresa tu registro")
registro = int(input())

print("\nIngresa la materia")
materia = input()

print("\nIngresa el plantel al que estas inscrito")
plantel = input()

print("\nIngresa la calificación que obtuviste")
calificacion = int(input())

# Se crea una arreglo con los elementos solicitados en la parte superior

datos = [nombre, registro, materia, plantel, calificacion]

print("\n\t--> Por motivos de seguridad el registro no será mostrado")

# Al mostrar los datos, la variable de 'registro' será ignorada y no será mostrada con ayuda del ciclo for

for x in datos:
    if x == registro:
        continue
    # Por cada dato ingresado, se mostrará el siguiente mensaje
    print("\nLos datos ingresados son:")
    print(x)