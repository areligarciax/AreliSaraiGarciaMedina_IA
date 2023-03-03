# Areli Sarai García Medina | 203010380
# Práctica 29 - Bucle For - El tipo de dato range()

print("- Elevar números al cuadrado -")

numero = ""

while True:
    numero = input("\nIngresa el número que quieres elevar al cuadrado\n")

    print("Para salir ingresa la tecla'x'")

    if numero == "x":
        print("... Saliendo del programa ...\n")
        break
    print("Resultado ->", int(numero) * int(numero))


    numeros = [136, 543, 673, 748]

for x in range (len(numeros)):
    print("E J E M P L O - Múltiplicación del número", numeros[x], "por sí mismo\t\t Resultado ->", numeros[x] * numeros[x])



