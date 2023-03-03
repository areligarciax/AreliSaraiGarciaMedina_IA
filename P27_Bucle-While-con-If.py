# Areli Sarai García Medina | 203010380
# Práctica 27 - Bucle While con Condicional If

print("- Bienvenido al programa -\n")
print("Para salir teclea la letra 'x'\n")
print("Introduce un número entero para contar hasta él desde 0")

num = int(input())
x = 0

while x <= num:
    print(x)

    if x == 500:
        print("\n'Disculpa, sólo podemos contar hasta 500'")
        break
    x += 1

else:
    print("\n--> ¡Hemos terminado de contar!")