# Areli Sarai García Medina | 203010380
# Práctica 23 - Comprobar datos en listas y tuplas

fruta = ['Arándano', 'Cereza', 'Ciruela', 'Frambuesa', 'Fresa', 'Granada', 'Lima', 'Limón', 'Mandarina', 'Manzana', 'Melón', 'Mora', 'Naranja', 'Pera', 'Piña', 'Plátano', 'Pomelo', 'Sandía', 'Uva']

entrada = input("Introduce el nombre de la fruta:\n")

if entrada in fruta:
    print("\n-> La fruta que buscas se encuentra en la lista")
else:
    print("\n-> La fruta que buscas NO está en la lista")


colores = ('Negro', 'Azul', 'Marrón', 'Gris', 'Verde', 'Naranja', 'Rosa', 'Púrpura', 'Rojo', 'Blanco', 'Amarillo')

entrada2 = input("\n\nIntroduce el nombre del color:\n")

if entrada2 in colores:
    print("\n-> El color que buscas se encuentra en la lista")
else:
    print("\n-> El color que buscas NO está en la lista")