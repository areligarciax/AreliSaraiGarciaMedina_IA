# Areli Sarai García Medina | 203010380
# Práctica 32 - Métodos con diccionarios


# Se crean un diccionario principal, con diccionarios anidados con sus elementos y atributos

categorias = {
    "cat1" : {
        "ID": "001",
        "Flor": "Rosas",
        "Precio": 250
        },

    "cat2": {
        "ID": "002",
        "Flor": "Lirios",
        "Precio": 300
        },

    "cat3": {
        "ID": "003",
        "Flor": "Margaritas",
        "Precio": 100
        },

    "cat4": {
        "ID": "004",
        "Flor": "Gardenias",
        "Precio": 230
        },

    "cat5": {
        "ID": "005",
        "Flor": "Claveles",
        "Precio": 280
        },

    "cat6": {
        "ID": "006",
        "Flor": "Orquídeas",
        "Precio": 350
        },

    "cat7": {
        "ID": "007",
        "Flor": "Tulipanes",
        "Precio": 320
        },

    "cat8": {
        "ID": "008",
        "Flor": "Peonias",
        "Precio": 370
        },

    "cat9": {
        "ID": "009",
        "Flor": "Dalias",
        "Precio": 400
        },

    "cat10": {
        "ID": "010",
        "Flor": "Crisantemos",
        "Precio": 390
        },

    "cat11": {
        "ID": "011",
        "Flor": "Camelias",
        "Precio": 450
        },

    "cat12": {
        "ID": "012",
        "Flor": "Flor de loto",
        "Precio": 480
        }
}

# Se actualizan (update()) los diccionarios agregando el atributo 'temporada' con su elemento

categorias.get("cat1").update({"Temporada": "Primavera"})
categorias.get("cat2").update({"Temporada": "Otoño"})
categorias.get("cat3").update({"Temporada": "Verano"})
categorias.get("cat4").update({"Temporada": "Primavera"})
categorias.get("cat5").update({"Temporada": "Otoño"})
categorias.get("cat6").update({"Temporada": "Verano"})
categorias.get("cat7").update({"Temporada": "Primavera"})
categorias.get("cat8").update({"Temporada": "Otoño"})
categorias.get("cat9").update({"Temporada": "Verano"})
categorias.get("cat10").update({"Temporada": "Primavera"})
categorias.get("cat11").update({"Temporada": "Otoño"})
categorias.get("cat12").update({"Temporada": "Verano"})


# Se obtiene el precio de las siguientes categorías y se elimina

categorias.get("cat1").pop("Precio")
categorias.get("cat5").pop("Precio")
categorias.get("cat7").pop("Precio")
categorias.get("cat9").pop("Precio")


# Se imprime lo que contienen los diccionarios

print(categorias["cat1"])
print("\n", categorias["cat2"])
print("\n", categorias["cat3"])
print("\n", categorias["cat4"])
print("\n", categorias["cat5"])
print("\n", categorias["cat6"])
print("\n", categorias["cat7"])
print("\n", categorias["cat8"])
print("\n", categorias["cat9"])
print("\n", categorias["cat10"])
print("\n", categorias["cat11"])
print("\n", categorias["cat12"])