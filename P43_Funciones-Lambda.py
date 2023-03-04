# Areli Sarai García Medina | 203010380
# Práctica 43 - Importar módulos y las funciones lambda

num1 = 0
num2 = 0

num1 = int(input("Introduce el primer número\n"))
num2 = int(input("Introduce el segundo número\n"))

suma = lambda resultado: round(num1 + num2, 3)
print("\nResultado de la suma", suma(num1+num2))

resta = lambda resultado: round(num1 - num2, 3)
print("Resultado de la resta", resta(num1-num2))

multiplicacion = lambda resultado: round(num1 * num2, 3)
print("Resultado de la multiplicación", multiplicacion(num1*num2))

division = lambda resultado: round(num1 / num2, 3)
print("Resultado de la división", division(num1/num2))