# Areli Sarai García Medina | 203010380
# Práctica 25 - Tips Condicionales

print("\t\t- B i e n v e n i d o -\n")
print("Introduce el valor de 'x'")
# Se crea la variable 'x' con entrada tipo entero
x = int(input())

print("Introduce el valor de 'y'")
# Se crea la variable 'y' con entrada tipo entero
y = int(input())

print("Introduce el valor de 'z'")
# Se crea la variable 'y' con entrada tipo entero
z = int(input())

# Se compara si 'x' es mayor a 'y' y mayor a 'z'
if x > y and x > z:
    print("El valor de 'x':", x, "es mayor que el valor de 'y':", y, "y de 'z':", z)

# Se compara si 'y' es mayor a 'x' y mayor a 'z'
if y > x and y > z:
    print("El valor de 'y':", y, "es mayor que el valor de 'x':", x, "y de 'z':", z)

# Se compara si 'z' es mayor a 'x' y mayor a 'y'
if z > x and z > y:
    print("El valor de 'z':", z, "es mayor que el valor de 'x':", x, "y de 'y':", y)


# En caso contrario de haber dos o más valores iguales, se imprime lo siguiente

else: print("\nEl valor de 'x', 'y' o 'z' son iguales")