# Areli Sarai García Medina | 203010380
# Práctica 40 - ¿Qué es la Herencia de clases? - Programación orientada a objetos


# Se crea la clase 'Usuario()' con sus atributos específicos
class Usuario():
	# Con el método '__init__' se inicializan los valores de la clase
	def __init__(self, nombre, apellido, registro, turno):
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	# Se crea la función 'imprimir_datos()'
	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)


# Se crea una nueva clase 'Fav()' con los atributos de la clase padre, mas nuevos atributos
class Fav(Usuario):
	# Con el método '__init__' se inicializan los valores de la clase
	def __init__(self, color, taste, musica):
		self.color = color
		self.taste = taste
		self.musica = musica

	# Se crea la función 'imprimir_datos2()' específica de la clase
	def imprimir_datos2(self):
		print('Color favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)


# Se crea el objeto 'usuario1' pasandole los atributos de la clase 'Usuario()' y se define que hay en ellos
usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
# Se imprimen los valores de 'usuario1'
usuario1.imprimir_datos()
# Se pasan los atributos de la clase 'Fav()' y se define que hay en ellos
usuario1 = Fav("Gold Rose", "Dulce", "Electrónica")
# Se imprimen además los valores de 'usuario1' clase 'Fav()'
usuario1.imprimir_datos2()

usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
# Se cambia el valor de 'apellido' y 'registro'
usuario2.apellido= "Rodríguez"
usuario2.registro = "20310389"
usuario2.imprimir_datos()

usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
# Se elimina el 'usuario3'
del usuario3

usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4 = Fav("Morado", "Salado", "Pop")

# Se imprimen los valores de 'usuario4' de las clases 'Usuario()' y 'Fav()'
usuario4.imprimir_datos()
usuario4.imprimir_datos2()

usuario5 = Usuario("Arlet", "Chávez", "223455", "Matutino")
usuario5.imprimir_datos()