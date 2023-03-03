# Areli Sarai García Medina | 203010380
# Práctica 25 - Tips Condicionales

print("\t\t- B i e n v e n i d o -\n")
print("Introduce el valor de 'x'")
x = int(input())

print("Introduce el valor de 'y'")
y = int(input())

print("Introduce el valor de 'z'")
z = int(input())

if x > y and x > z:
    print("El valor de 'x':", x, "es mayor que el valor de 'y':", y, "y de 'z':", z)

if y > x and y > z:
    print("El valor de 'y':", y, "es mayor que el valor de 'x':", x, "y de 'z':", z)

if z > x and z > x:
    print("El valor de 'z':", z, "es mayor que el valor de 'x':", x, "y de 'y':", y)

else: print("\nEl valor de 'x', 'y' o 'z' son iguales")