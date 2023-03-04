# Areli Sarai García Medina | 203010380
# Práctica 39 - Como declarar clases vacías con pass y eliminar objetos - Programación orientada a objetos

class Usuario():
	def __init__(self, nombre, apellido, registro, turno):
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)

class Fav():
	def __init__(self, color, taste, musica):
		self.color = color
		self.taste = taste
		self.musica = musica

	def imprimir_datos(self):
		print('\nColor favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)
	pass

usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
usuario1.imprimir_datos()

usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
usuario2.apellido= "Rodríguez"
usuario2.registro = "20310389"
usuario2.imprimir_datos()

usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
del usuario3

usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4.imprimir_datos()

usuario5 = Usuario("Arlet", "Chávez", "223455", "Matutino")
usuario5.imprimir_datos()