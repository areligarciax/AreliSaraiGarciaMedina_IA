# Areli Sarai García Medina | 203010380
# Práctica 16 - Método Sort() y Sorted()

colores = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura', 'rojo', 'blanco', 'amarillo']

print("La lista de colores ordenada alfabéticamente ascendientemente es:", sorted(colores))

print("El primer elemento de la lista es:", colores[0])
print("El útimo elemento de la lista es:", colores[-1])

colores.sort()

print("\nAhora, el primer elemento de la lista es:", colores[0])
print("Y el último elemento de la lista por su nombre es:", colores[-1])

colores.sort(reverse=True)
print("\nLa lista de colores ordenada alfabéticamente descendientemente es:", colores)
print("\nAsí, el primer elemento de la lista será:", colores[0])
print("Y el último elemento de la lista por su nombre es:", colores[-1])