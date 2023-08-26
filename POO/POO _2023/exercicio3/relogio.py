class Relogio:

	def __init__(self, horas: int, minutos: int, segundos: int):
		self.horas = self.set_hora(horas)
		self.minutos = self.set_minuto(minutos)
		self.segundos = self.set_segundo(segundos)

	def get_hora_como_string(self) -> str:
		return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'


relogio = Relogio(12,10,15)
relogio.get_hora_como_string()
print(relogio)
