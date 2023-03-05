# Areli Sarai García Medina | 203010380
# Práctica 41 - Como heredar propiedades __init__ - Programación orientada a objetos


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
	def __init__(self, nombre, apellido, registro, turno, color, taste, musica):
		# Se mandan llamar los atributos de la clase padre y se le agregan los nuevos atributos
		Usuario.__init__(self, nombre, apellido, registro, turno)
		self.color = color
		self.taste = taste
		self.musica = musica

	# Se crea la función 'imprimir_datos2()' específica de la clase
	def imprimir_datos2(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nColor favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)

# Se declara en una misma linea el valor de los atributos de la clase padre con la clase hija
usuario1 = Fav("Areli", "García", "20310380", "Vespertino", "Gold Rose", "Dulce", "Electrónica")
# Se imprime en una sola linea todos los elementos
usuario1.imprimir_datos2()

usuario2 = Fav("Cecille", "Bechelani", "2436689", "Matutino", "Negro", "Salado", "Hip Hop")
usuario2.imprimir_datos2()

usuario3 = Fav("Josué", "Medina", "256677", "Matutino", "Verde", "Salado", "Rap")
usuario3.imprimir_datos2()

usuario4 = Fav("Sarah", "Veazey", "234567", "Vespertino", "Morado", "Salado", "Pop")
usuario4.imprimir_datos2()

usuario5 = Fav("Arlet", "Chávez", "223455", "Matutino", "Rosa", "Dulce", "Pop")
usuario5.imprimir_datos2()