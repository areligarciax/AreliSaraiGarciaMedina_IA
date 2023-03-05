# Areli Sarai García Medina | 203010380
# Práctica 34 - Argumentos arbitrarios - Como utilizar *args


# Se crea la función flores() y se le pasan los argumentos 'categoria', 'temporada' y '*args'
# '*args' sirve para poner argumentos de manera arbitraria y se puedan llenar libremente
def flores(categoria, temporada, *args):
    print("Categoría: " + categoria)
    print("Temporada: " + temporada)


    # Por cada argumento que se defina, se imprimirá 'Flor:' seguido del valor definido
    for x in args:
        print("Flor: " + x)


# Se definen los argumentos arbitrarios en un string
nombre = ["Rosas", "Margaritas", "Girasoles", "Tulipanes", "Lirios", "Flor de Loto", "Petunias", "Lilies"]


# Se manda imprimir la 'categoría', 'temporada' seguido de los argumentos 'nombre'
flores("Flores de Temporada", "Primavera", *nombre)