# Areli Sarai García Medina | 203010380
# Práctica 24 - Multiples condiciones If

# Se imprime el siguiente mensaje

print('\t\t- Bienvenido a "Florería Lilies" -\n\n'
      '¿Qué te gustaría comprar?\n'
      '1. Tulipanes - $200\n'
      '2. Rosas - $100\n'
      '3. Margaritas - $80\n'
      '4. Girasoles - $120\n'
      '5. Orquídeas - $280\n'
      '6. Bugambilias - $190\n'
      '7. Flor de loto - $300\n')

# Se crea un arreglo vacío
comprar = []

# Se declara la variable con valor inicial de 500
dinero = 500

# Se asigna el precio de los elementos
tulipanes = 450
rosas = 300
margaritas = 290
girasoles = 320
orquideas = 560
bugambilias = 400
flordeloto = 700


print("Escoge un valor entre 1 y 7")

# Se crea la variable 'entrada' para ingresar datos tipo entero
entrada = int(input())

# Se agrega entrada a comprar
comprar.append(entrada)


# Se comienza a comparar la variable entrada con el número de casos, para que realice las operaciones que allí se indican
if 1 in comprar:
      dinero = dinero-tulipanes

elif 2 in comprar:
      dinero = dinero-rosas

elif 3 in comprar:
      dinero = dinero-margaritas

elif 4 in comprar:
            dinero = dinero-girasoles

elif 5 in comprar:
            dinero = dinero-orquideas

elif 6 in comprar:
            dinero = dinero-bugambilias

elif 7 in comprar:
            dinero = dinero-flordeloto

# En caso de ingresar un número diferente de 1 al 7, se imprime el siguiente mensaje
else:
      print("\n-- Opción no valida. Introduce un número entre 1 y 7.")


# Si la variable dinero es menor a 0, se imprime el siguiente mensaje
if dinero < 0:
      print("\n¡Ya no tienes más dinero para gastar en flores!")


# Se imprime que cantidad es la que queda después de la "compra"
print("Te quedan $" + str(dinero) + " pesos")