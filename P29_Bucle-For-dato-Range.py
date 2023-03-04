# Areli Sarai García Medina | 203010380
# Práctica 29 - Bucle For - El tipo de dato range()

print("- Elevar números al cuadrado -")

# Se declara la variable 'numero' de forma vacía
numero = ""

# Se crea un bucle while que mientras sea verdadero ingresará para realizar las operaciones especificadas dentro de él
while True:
    numero = input("\nIngresa el número que quieres elevar al cuadrado\n")

    print("Para salir ingresa la tecla'x'")

    # Si se ingresa la tecla 'x' el bucle se hará falso y saldrá del programa
    if numero == "x":
        print("... Saliendo del programa ...\n")
        break
    # Se muestra el resultado de elevar el número al cuadrado
    print("Resultado ->", int(numero) * int(numero))

    # ------------------------------------------------------------------------------------------------------------------------------

    # Otra forma de elevar al cuadrado es la siguiente

    # Declaramos el arreglo con el valor de las variables

    numeros = [136, 543, 673, 748]

# El ciclo for observa los valores que se encuentran en el arreglo y con ayuda de range() ve cuantas veces se tiene que iterar
# (En este caso se iterará 4 veces porque con ayuda de len() se entrega cuantos elementos hay en el arreglo

for x in range(len(numeros)):
    print("E J E M P L O - Múltiplicación del número", numeros[x], "por sí mismo\t\t Resultado ->",
          # Se multiplica el número por si mismo para elevarlo al cuadrado
          numeros[x] * numeros[x])