# Areli Sarai García Medina | 203010380
# Práctica 15 - Método Insert()

# Creamos una lista con sus objetos

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']


# Eliminamos los objetos por su posición

del fruta[4]
del fruta[-5]

# Eliminamos los objetos por string

fruta.remove("Granada")
fruta.remove("Pomelo")
fruta.remove("Manzana")

# Agregamos los objetos en la posición que queramos

fruta.insert(4,"Coco")
fruta.insert(-3, "Guayaba")
fruta.insert(7, "Kiwi")


# Imprimimos el contenido de la lista

print("Lista de frutas:", fruta)