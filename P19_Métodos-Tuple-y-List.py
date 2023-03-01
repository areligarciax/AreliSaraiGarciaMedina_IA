# Areli Sarai García Medina | 203010380
# Práctica 19 - Cómo convertir tuplas a listas y viceversa

elementos = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura', 'rojo', 'blanco', 'amarillo', 'Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']
ceti = ("Inteligencia Artificial", "Areli García","Número de registro:", 20000000, 310000, 380)

print("La lista de elementos que tenemos es:", elementos)
print("La tupla que tenemos es:", ceti)

telementos = tuple(elementos)
print("\nLa tupla de elementos que tenemos es:", telementos)

lceti = list(ceti)
print("La lista que tenemos ahora es:", lceti)

print("\nMateria:", ceti[0])
print("Alumna:", ceti[1])
print(ceti[2], + ceti[3] + ceti[4] + ceti[5])