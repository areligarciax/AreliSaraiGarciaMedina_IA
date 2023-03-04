# Areli Sarai García Medina | 203010380
# Práctica 38 - ¿Qué es self? - Cambiar valores en objetos - Programación orientada a objetos

class Usuario():
	def __init__(self, nombre, apellido, registro, turno):
		self.nombre = nombre
		self.apellido = apellido
		self.registro = registro
		self.turno = turno

	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro,  '\nTurno:', self.turno)

usuario1 = Usuario("Areli", "García", "20310380", "Vespertino")
usuario1.imprimir_datos()

usuario2 = Usuario("Cecille", "Bechelani", "2436689", "Matutino")
usuario2.apellido= "Rodríguez"
usuario2.registro = "20310389"
usuario2.imprimir_datos()

usuario3 = Usuario("Josué", "Medina", "256677", "Matutino")
usuario3.imprimir_datos()

usuario4 = Usuario("Sarah", "Veazey", "234567", "Vespertino")
usuario4.apellido = "Viudez"
usuario4.registro = "20310788"
usuario4.imprimir_datos()