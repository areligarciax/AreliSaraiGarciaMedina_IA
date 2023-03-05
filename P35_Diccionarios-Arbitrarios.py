# Areli Sarai García Medina | 203010380
# Práctica 35 - **kwargs - Diccionarios arbitrarios


# Se crea la función flores() con argumentos arbitrarios
def flores(**kwargs):
    # Se imprime del primer al último elemento del diccionario
    print("La primera flor es: " + kwargs["flor1"])
    print("La segunda flor es: " + kwargs["flor2"])
    print("La tercer flor es: " + kwargs["flor3"])
    print("La cuarta flor es: " + kwargs["flor4"])
    print("La quinta flor es: " + kwargs["flor5"])
    print("La sexta flor es: " + kwargs["flor6"] + "\n\n")

# Se define el diccionario 'flores' con sus elementos
flores(flor1 = "Rosa", flor2 = "Tulipan", flor3 = "Margarita", flor4 = "Lirio", flor5 = "Flor de Loto", flor6 = "Peonia")



# Se crea la función frutas() con argumentos arbitrarios
def frutas(**kwargs):
    # Se imprime del primer al último elemento del diccionario
    print("La primera fruta es: " + kwargs["fruta1"])
    print("La segunda fruta es: " + kwargs["fruta2"])
    print("La tercer fruta es: " + kwargs["fruta3"])
    print("La cuarta fruta es: " + kwargs["fruta4"])
    print("La quinta fruta es: " + kwargs["fruta5"])
    print("La sexta fruta es: " + kwargs["fruta6"])


# Se define el diccionario 'frutas' con sus elementos
frutas(fruta1 = "Fresa", fruta2 = "Manzana", fruta3 = "Uva", fruta4 = "Sandía", fruta5 = "Kiwi", fruta6 = "Mora azul")