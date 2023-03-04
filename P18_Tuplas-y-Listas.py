# Areli Sarai García Medina | 203010380
# Práctica 18 - Crear y manejar tuplas - Diferencias con las listas

# Creamos una lista con sus elementos

elementos = ['negro', 'azul', 'marrón', 'gris', 'verde', 'naranja', 'rosa', 'púrpura', 'rojo', 'blanco', 'amarillo', 'Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']


# Creamos una tupla con sus elementos

ceti = ("Inteligencia Artificial", "Areli García","Número de registro:", 20000000, 310000, 380)


# Imprimimos la lista

print("La lista de elementos que tenemos es:", elementos)


# Imprimimos la tupla

print("La tupla que tenemos es:", ceti)


# Imprimimos y mandamos llamar los elementos de la tupla

print("\nMateria:", ceti[0])
print("Alumna:", ceti[1])
print(ceti[2], + ceti[3] + ceti[4] + ceti[5])