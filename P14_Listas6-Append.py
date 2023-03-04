# Areli Sarai García Medina | 203010380
# Práctica 14 - Método Append()

# Declaramos la lista con sus objetos

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']


# Eliminamos el objeto por su posición

del fruta[4]
del fruta[-5]

# Eliminamos el objeto con string

fruta.remove("Granada")
fruta.remove("Pomelo")
fruta.remove("Manzana")


# Agregamos los objetos al final de la lista

fruta.append("Fresa")
fruta.append("Manzana")


# Imprimimos la lista

print("Lista de frutas:", fruta)