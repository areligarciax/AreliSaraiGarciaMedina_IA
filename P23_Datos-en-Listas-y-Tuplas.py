# Areli Sarai García Medina | 203010380
# Práctica 23 - Comprobar datos en listas y tuplas

# Creamos la lista con sus elementos

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']


# Declaramos la variable 'entrada' como entrada de datos tipo string

entrada = input("Introduce el nombre de la fruta:\n")

# Comprobamos que el string ingresado este en la lista

if entrada in fruta:
    print("\n-> La fruta que buscas se encuentra en la lista")


# En caso contrario de no estar, se imprime el siguiente mensaje
else:
    print("\n-> La fruta que buscas NO está en la lista")


# Creamos la tupla con sus elementos

colores = ('Negro', 'Azul', 'Marrón', 'Gris', 'Verde', 'Naranja', 'Rosa', 'Púrpura', 'Rojo', 'Blanco', 'Amarillo')


# Declaramos la variable 'entrada2' como entrada de datos tipo string

entrada2 = input("\n\nIntroduce el nombre del color:\n")


# Comprobamos que el string ingresado este en la tupla

if entrada2 in colores:
    print("\n-> El color que buscas se encuentra en la lista")

# En caso contrario de no encontrar coincidencias, se imprimirá el siguiente mensaje
else:
    print("\n-> El color que buscas NO está en la lista")