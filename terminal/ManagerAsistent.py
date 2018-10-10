import managerConf
import funcionesVarias
import antvirus
import cifrado

class Asistente(object):
	def __init__(self, **kwargs):
		self.nombre = kwargs["nombre"]
		self.usuario = kwargs["usuario"]
		self.genero = kwargs["genero"]
		self.comando = lambda x: return str(open(x, "r").read()) (kwargs["comandos"])
		self.response_default = kwargs["respuesta_automatica"]

	def play(*args):
		if args[0] == True:
			pass

		