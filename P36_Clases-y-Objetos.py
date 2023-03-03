# Areli Sarai García Medina | 203010380
# Práctica 36 - Clases y objetos - Programación orientada a objetos

class Usuario:
	nombre = ''
	apellido = ''
	registro = ''
	turno = ''


	def imprimir_datos(self):
		print('\nNombre:', self.nombre, '\nApellido:', self.apellido, '\nRegistro:', self.registro, '\nTurno:', self.turno)

usuario1 = Usuario()

usuario1.nombre = 'Areli'
usuario1.apellido = 'García'
usuario1.registro = 20310380
usuario1.turno = 'Vespertino'


usuario2 = Usuario()

usuario2.nombre = 'Cecille'
usuario2.apellido = 'Bechelani'
usuario2.registro = 20476499
usuario2.turno = 'Vespertino'


usuario3 = Usuario()

usuario3.nombre = 'Arlet'
usuario3.apellido = 'Chávez'
usuario3.registro = 25666568
usuario3.turno = 'Matutino'


usuario4 = Usuario()

usuario4.nombre = 'Josué'
usuario4.apellido = 'Medina'
usuario4.registro = 23875900
usuario4.turno = 'Matutino'


usuario5 = Usuario()

usuario5.nombre = 'Ángel'
usuario5.apellido = 'Espinoza'
usuario5.registro = 26567765
usuario5.turno = 'Vespertino'


usuario6 = Usuario()

usuario6.nombre = 'Sarah'
usuario6.apellido = 'Veazey'
usuario6.registro = 26565786
usuario6.turno = 'Matutino'


usuario1.imprimir_datos()
usuario2.imprimir_datos()
usuario3.imprimir_datos()
usuario4.imprimir_datos()
usuario5.imprimir_datos()
usuario6.imprimir_datos()