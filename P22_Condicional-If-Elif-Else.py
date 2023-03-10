# Areli Sarai García Medina | 203010380
# Práctica 22 - El condicional If Elif Else e Input, Entrada de Datos

# Declaramos la variable edad como entrada de datos tipo entero

edad = int(input("¿Cuántos años tienes?\n"))

# Con ayuda de los if y elif, el programa evaluará a que edad pertenece el individuo y entrará al caso en específico

if edad<=0:
    print("No puedes tener esa edad a menos que cuentes tu edad en meses")
elif edad>=1 and edad<=5:
    print("Estás en la etapa:'Primera Infancia'")
elif edad>5 and edad<=11:
    print("Estás en la etapa:'Infancia'")
elif edad>11 and edad<=18:
    print("Estás en la etapa:'Adolescencia'")
elif edad>18 and edad<=26:
    print("Estás en la etapa:'Juventud'")
elif edad>26 and edad<=59:
    print("Estás en la etapa:'Adultez'")
elif edad>59 and edad<=100:
    print("Estás en la etapa:'Vejez'")

# En caso de que ingrese algun valor no permitido, se imprimirá el siguiente mensaje
else:
    print("-> Edad no válida")