# Areli Sarai García Medina | 203010380
# Práctica 39 - Como declarar clases vacías con pass y eliminar objetos - Programación orientada a objetos


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

# Se crea una nueva clase 'Fav()' con nuevos atributos
class Fav():
	# Con el método '__init__' se inicializan los valores de la clase
	def __init__(self, color, taste, musica):
		self.color = color
		self.taste = taste
		self.musica = musica

	# Se crea la función 'imprimir_datos2()' específica de la clase
	def imprimir_datos2(self):
		print('\nColor favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)
	# Por el momento, no queremos que se utilice esta clase, por lo que la pasamos con ayuda de 'pass'
	pass


# Se crea el objeto 'usuario1' pasandole los atributos de la clase y se define que hay en ellos
usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
# Se imprimen los valores de 'usuario1'
usuario1.imprimir_datos()

usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
usuario2.apellido= "Rodríguez"
usuario2.registro = "20310389"
usuario2.imprimir_datos()

usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
# Se elimina el 'usuario3'
del usuario3

usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4.imprimir_datos()

usuario5 = Usuario("Arlet", "Chávez", "223455", "Matutino")
usuario5.imprimir_datos()