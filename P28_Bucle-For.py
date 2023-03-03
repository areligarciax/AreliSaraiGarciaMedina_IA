# Areli Sarai García Medina | 203010380
# Práctica 28 - Bucle For

print("\t\t- B I E N V E N I D O -\n")
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

datos = [nombre, registro, materia, plantel, calificacion]

print("\n\t--> Por motivos de seguridad el registro no será mostrado")

for x in datos:
    if x == registro:
        continue
    print("\nLos datos ingresados son:")
    print(x)