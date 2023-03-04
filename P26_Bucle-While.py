# Areli Sarai García Medina | 203010380
# Práctica 26 - Bucle While

# Se imrpimen los siguientes mensajes
print("- Bienvenido al programa -\n")
print("Para salir teclea la letra 'x'\n")
print("Introduce un número entero para contar hasta él desde 0")


# Se crea la variable 'num' con entrada tipo entero
num = int(input())
# Se inicializa 'x' con valor de 0
x = 0

# Se crea un bucle al que entrará hasta que 'x' llegue al número ingresado
# Por lo tanto el programa imprimirá todos los valores hasta llegar al valor ingresado

while x <= num:
    print(x)
    # El valor de 'x' va sumando 1 cada vez que entra al bucle
    x += 1