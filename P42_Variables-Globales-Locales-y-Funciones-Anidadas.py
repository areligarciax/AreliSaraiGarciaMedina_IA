# Areli Sarai García Medina | 203010380
# Práctica 42 - Variables globales, locales y funciones anidadas

num1 = 130602
num2 = 557

def suma():
    global resultado1
    resultado1 = num1 + num2

def resta():
    global resultado2
    resultado2 = num1 - num2

def multiplicacion():
    global resultado3
    resultado3 = num1 * num2

def division():
    global resultado4
    resultado4 = num1 / num2

suma()
print(num1, " + ", num2, " = ", resultado1)

resta()
print(num1, " -", num2, " = ", resultado2)

multiplicacion()
print(num1, " *", num2, " = ", resultado3)

division()
print(num1, " / ", num2, " = ", resultado4)

