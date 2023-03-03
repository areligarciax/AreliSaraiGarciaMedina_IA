# Areli Sarai García Medina | 203010380
# Práctica 34 - Argumentos arbitrarios - Como utilizar *args

def flores(categoria, temporada, *args):
    print("Categoría: " + categoria)
    print("Temporada: " + temporada)

    for x in args:
        print("Flor: " + x)

nombre = ["Rosas", "Margaritas", "Girasoles", "Tulipanes", "Lirios", "Flor de Loto", "Petunias", "Lilies"]

flores("Flores de Temporada", "Primavera", *nombre)