# Areli Sarai García Medina | 203010380
# Práctica 50 - Manejo de excepciones

def iniciar():
    print("\t\t\t- B I E N V E N I D O -")
    print("... ¿Qué deseas hacer? ...")
    print("\nMenú")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")

    global operacion
    operacion = input("Ingresa una de las opciones\n")

reinicio = True
num1 = 0
num2 = 0
resultado = 0



while reinicio:
    try:
        iniciar()

        if operacion == "1":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))
            resultado = num1 + num2

        elif operacion == "2":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 - num2

        elif operacion == "3":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 * num2

        elif operacion == "4":
            num1 = int(input("\nIntroduce el primer número\n"))
            num2 = int(input("Introduce el segundo número\n"))

            resultado = num1 / num2

        else:
            print('\n\n- Lo siento, ha ocurrido un error -')
            continue

        print("Resultado = ", resultado)
        resultado = 0

    except ValueError:
        print("\n\n- No has introducido un número. Vuelve a intentarlo. -")

    finally:
        pregunta = input("\n¿Quieres seguir haciendo operaciones? (Teclea 'x' para salir)\n")
        if pregunta == "x":
            reinicio = False
        else:
            print("\nMuy bien, sigamos con las operaciones:)\n")