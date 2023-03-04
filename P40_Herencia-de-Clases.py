# Areli Sarai García Medina | 203010380
# Práctica 40 - ¿Qué es la Herencia de clases? - Programación orientada a objetos

class Usuario():
	def __init__(self, nombre, apellido, registro, turno):
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)

class Fav(Usuario):
	def __init__(self, color, taste, musica):
		self.color = color
		self.taste = taste
		self.musica = musica

	def imprimir_datos2(self):
		print('Color favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)


usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
usuario1.imprimir_datos()
usuario1 = Fav("Gold Rose", "Dulce", "Electrónica")
usuario1.imprimir_datos2()

usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
usuario2.apellido= "Rodríguez"
usuario2.registro = "20310389"
usuario2.imprimir_datos()

usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
del usuario3

usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4.imprimir_datos()
usuario4 = Fav("Morado", "Salado", "Pop")
usuario4.imprimir_datos2()

usuario5 = Usuario("Arlet", "Chávez", "223455", "Matutino")
usuario5.imprimir_datos()