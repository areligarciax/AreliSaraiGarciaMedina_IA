# Areli Sarai García Medina | 203010380
# Práctica 19 - Cómo convertir tuplas a listas y viceversa

# Creamos la lista con sus elementos

elementos = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura', 'rojo', 'blanco', 'amarillo', 'Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']


# Creamos la tupla con sus elementos

ceti = ("Inteligencia Artificial", "Areli García","Número de registro:", 20000000, 310000, 380)



# Imprimimos la lista y la tupla

print("La lista de elementos que tenemos es:", elementos)
print("La tupla que tenemos es:", ceti)

# Cambiamos la lista por una tupla
telementos = tuple(elementos)

#Imprimimos
print("\nLa tupla de elementos que tenemos es:", telementos)


# Cambiamos la tupla por una lista
lceti = list(ceti)

# Imprimimos
print("La lista que tenemos ahora es:", lceti)

print("\nMateria:", ceti[0])
print("Alumna:", ceti[1])
print(ceti[2], + ceti[3] + ceti[4] + ceti[5])