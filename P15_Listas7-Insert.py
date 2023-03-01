# Areli Sarai García Medina | 203010380
# Práctica 15 - Método Insert()

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']

del fruta[4]
del fruta[-5]

fruta.remove("Granada")
fruta.remove("Pomelo")
fruta.remove("Manzana")

fruta.insert(4,"Coco")
fruta.insert(-3, "Guayaba")
fruta.insert(7, "Kiwi")

print("Lista de frutas:", fruta)