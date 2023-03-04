# Areli Sarai García Medina | 203010380
# Práctica 16 - Método Sort() y Sorted()

# Creamos una lista con sus objetos

colores = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura', 'rojo', 'blanco', 'amarillo']

# Ordenamos alfabéticamente la lista de manera ascendiente de manera momentanea

print("La lista de colores ordenada alfabéticamente ascendientemente es:", sorted(colores))


# Imprimimos el primer y último elemento de la lista

print("El primer elemento de la lista es:", colores[0])
print("El útimo elemento de la lista es:", colores[-1])


# Ordenamos alfabéticamente la lista de manera ascendiente de manera permanente

colores.sort()

# Imprimimos el resultado

print("\nAhora, el primer elemento de la lista es:", colores[0])
print("Y el último elemento de la lista por su nombre es:", colores[-1])


# Ordenamos la lista alfabéticamente de manera descendiente

colores.sort(reverse=True)

# Imprimimos el resultado

print("\nLa lista de colores ordenada alfabéticamente descendientemente es:", colores)
print("\nAsí, el primer elemento de la lista será:", colores[0])
print("Y el último elemento de la lista por su nombre es:", colores[-1])