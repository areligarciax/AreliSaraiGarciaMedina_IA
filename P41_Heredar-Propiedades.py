# Areli Sarai García Medina | 203010380
# Práctica 41 - Como heredar propiedades __init__ - Programación orientada a objetos

class Usuario():
	def __init__(self, nombre, apellido, registro, turno):
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)

class Fav(Usuario):
	def __init__(self, nombre, apellido, registro, turno, color, taste, musica):
		Usuario.__init__(self, nombre, apellido, registro, turno)
		self.color = color
		self.taste = taste
		self.musica = musica

	def imprimir_datos2(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nColor favorito:', self.color, '\nDulce o Salado:', self.taste, '\nMúsica Favorita:', self.musica)


usuario1 = Fav("Areli", "García", "20310380", "Vespertino", "Gold Rose", "Dulce", "Electrónica")
usuario1.imprimir_datos2()


usuario2 = Fav("Cecille", "Bechelani", "2436689", "Matutino", "Negro", "Salado", "Hip Hop")
usuario2.imprimir_datos2()

usuario3 = Fav("Josué", "Medina", "Verde", "256677", "Matutino", "Salado", "Rap")
usuario3.imprimir_datos2()

usuario4 = Fav("Sarah", "Veazey", "Morado", "234567", "Vespertino", "Salado", "Pop")
usuario4.imprimir_datos2()


usuario5 = Fav("Arlet", "Chávez", "223455", "Matutino", "Rosa", "Dulce", "Pop")
usuario5.imprimir_datos2()