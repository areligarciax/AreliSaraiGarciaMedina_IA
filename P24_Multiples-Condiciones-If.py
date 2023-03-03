# Areli Sarai García Medina | 203010380
# Práctica 24 - Multiples condiciones If

print('\t\t- Bienvenido a "Florería Lilies" -\n\n'
      '¿Qué te gustaría comprar?\n'
      '1. Tulipanes - $200\n'
      '2. Rosas - $100\n'
      '3. Margaritas - $80\n'
      '4. Girasoles - $120\n'
      '5. Orquídeas - $280\n'
      '6. Bugambilias - $190\n'
      '7. Flor de loto - $300\n')

comprar = []
dinero = 500

tulipanes = 450
rosas = 300
margaritas = 290
girasoles = 320
orquideas = 560
bugambilias = 400
flordeloto = 700


print("Escoge un valor entre 1 y 7")
entrada = int(input())
comprar.append(entrada)

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

else:
      print("\n-- Opción no valida. Introduce un número entre 1 y 7.")

if dinero < 0:
      print("\n¡Ya no tienes más dinero para gastar en flores!")

print("Te quedan $" + str(dinero) + " pesos")