# Areli Sarai García Medina | 203010380
# Práctica 13 - Método Pop()

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']

del fruta[0]
del fruta[-5]

fruta.remove("Granada")
fruta.remove("Pomelo")

gLista = fruta.pop(5)
gLista2 = fruta.pop(-7)

print("Lista de frutas:", fruta)
print("\nElemento '1' guardado y eliminado de la lista:", gLista)
print("Elemento '2' guardado y eliminado de la lista:", gLista2)