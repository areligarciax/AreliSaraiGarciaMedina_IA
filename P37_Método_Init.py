# Areli Sarai García Medina | 203010380
# Práctica 37 - El método __init__ - Programación orientada a objetos


# Se crea la clase 'Usuario()' con sus atributos específicos
class Usuario():
	# Con el método '__init__' se inicializan los valores de la clase
	def __init__(self, nombre, apellido, registro, turno):
		# Con el self se hace referencia al nombre del objeto en el que se encuentra escrito
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	# Se crea la función 'imprimir_datos()'
	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)

# Se crea el objeto 'usuario1' pasandole los atributos de la clase y se define que hay en ellos
usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
usuario1.imprimir_datos()

# Se crea el objeto 'usuario2' pasandole los atributos de la clase y se define que hay en ellos
usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
usuario2.imprimir_datos()

# Se crea el objeto 'usuario3' pasandole los atributos de la clase y se define que hay en ellos
usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
usuario3.imprimir_datos()

# Se crea el objeto 'usuario4' pasandole los atributos de la clase y se define que hay en ellos
usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4.imprimir_datos()