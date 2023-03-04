# Areli Sarai García Medina | 203010380
# Práctica 13 - Método Pop()


# Declaramos la lista con sus objetos

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']

# Eliminamos el objeto por su posición

del fruta[0]
del fruta[-5]

# Eliminamos el objeto utilizando string

fruta.remove("Granada")
fruta.remove("Pomelo")

# Guardamos en una variable y eliminamos el objeto

gLista = fruta.pop(5)
gLista2 = fruta.pop(-7)

# Imprimimos el resultado

print("Lista de frutas:", fruta)
print("\nElemento '1' guardado y eliminado de la lista:", gLista)
print("Elemento '2' guardado y eliminado de la lista:", gLista2)