# Areli Sarai García Medina | 203010380
# Práctica 50 - Manejo de excepciones

# Se crea la función iniciar()
def iniciar():
    print("\t\t\t- B I E N V E N I D O -")
    print("... ¿Qué deseas hacer? ...")
    print("\nMenú")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")

    # Se hace global la variable 'operacion' para poder utilizarla después
    global operacion
    # Se le pregunta al usuario que ingrese una opción (del 1 al 4)
    operacion = input("Ingresa una de las opciones\n")

# 'reinicio' se pone como True para que al mandarla a llamar entre al bucle
reinicio = True
# Se declara e inicializan las variables
num1 = 0
num2 = 0
resultado = 0


# Se crea el bucle while
while reinicio:
    # Con la ayuda de try, el programa "prueba" el código
    try:
        # Se manda llamar la función 'iniciar()'
        iniciar()

        # Si se ingresa '1', se pediran dos números y se efectuará la suma
        if operacion == "1":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))
            resultado = num1 + num2

        # Si se ingresa '2', se pediran dos números y se efectuará la resta
        elif operacion == "2":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 - num2

        # Si se ingresa '3', se pediran dos números y se efectuará la multiplicación
        elif operacion == "3":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 * num2

        # Si se ingresa '4', se pediran dos números y se efectuará la división
        elif operacion == "4":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 / num2

        else:
            # En dado caso de no ingresar ninguna de las opciones (del 1 al 4) se imprimirá el siguiente mensaje
            print('\n\n- Lo siento, ha ocurrido un error -')
            continue
        # Se imprime el resultado de la operación
        print("Resultado = ", resultado)
        # Resultado vuelve a 0
        resultado = 0

    except ValueError:
        # Si no se ha introducido un valor numérico, se imprimirá el siguiente mensaje
        print("\n\n- No has introducido un número. Vuelve a intentarlo. -")

    finally:
        # Después de cada operación, se preguntará al usuario lo siguiente esperando la entrada de un valor
        pregunta = input("\n¿Quieres seguir haciendo operaciones? (Teclea 'x' para salir)\n")
        if pregunta == "x":
            # Si el usuario ingresa la tecla 'x', 'reinicio' se hará false y no entrará de nuevo al bucle, finalizando el programa
            reinicio = False
        else:
            # Si teclea cualquier otra tecla, volverá a ingresar al ciclo while para seguir haciendo operaciones
            print("\nMuy bien, sigamos con las operaciones:)\n")