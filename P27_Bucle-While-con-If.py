# Areli Sarai García Medina | 203010380
# Práctica 27 - Bucle While con Condicional If

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

# Pero con la excepción del if, el programa solo podrá contar hasta el número 500, y saldrá del bucle
    if x == 500:
        print("\n'Disculpa, sólo podemos contar hasta 500'")
        break
    x += 1
    
# Si se ingresa un numero menor a 500, al finalizar se imprimirá el siguiente mensaje
else:
    print("\n--> ¡Hemos terminado de contar!")