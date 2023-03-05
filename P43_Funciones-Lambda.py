# Areli Sarai García Medina | 203010380
# Práctica 43 - Importar módulos y las funciones lambda

# Se declaran las variables 'num1' y 'num2' y se inicializan en 0
num1 = 0
num2 = 0


# Se pide que ingresen los valores de 'num1' y 'num2' de  tipo entero
num1 = int(input("Introduce el primer número\n"))
num2 = int(input("Introduce el segundo número\n"))



# Con la funcion lamda se realiza la operacion una vez, por lo que no ocupa espacio en la memoria
# Con el método round() se redondean los números fraccionarios a 3 decimales
suma = lambda resultado: round(num1 + num2, 3)
# Se imprime el resultado de la suma de los dos números
print("\nResultado de la suma", suma(num1+num2))

# Con el método round() se redondean los números fraccionarios a 2 decimales
resta = lambda resultado: round(num1 - num2, 2)
# Se imprime el resultado de la resta de los dos números
print("Resultado de la resta", resta(num1-num2))

multiplicacion = lambda resultado: round(num1 * num2, 3)
# Se imprime el resultado de la multiplicación de los dos números
print("Resultado de la multiplicación", multiplicacion(num1*num2))

division = lambda resultado: round(num1 / num2, 4)
# Con el método round() se redondean los números fraccionarios a 4 decimales
# Se imprime el resultado de la división de los dos números
print("Resultado de la división", division(num1/num2))