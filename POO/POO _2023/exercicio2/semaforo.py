AMARELO = "amarelo"
VERMELHO = "vermelho"
VERDE = "verde"


class Timer:

  def __init__(self, ligado: bool):
    self.esta_ligado = ligado
    self.valor_atual: int | None = None


class Lampada:
  def __init__(self, cor: str, ligado: bool):
    self.cor = cor
    self.esta_ligada = ligado

  def acender(self):
    self.esta_ligada = True
  
  def apagar(self):
    self.esta_ligada = False




class Semaforo:
    contador = 0
    
    
    def __init__(self):
        self.incrementa_contador()
        self.lampada_verde = Lampada(cor=VERDE, ligado=False)
        self.lampada_amarela = Lampada(cor=AMARELO, ligado=False)
        self.lampada_vermelha = Lampada(cor=VERMELHO, ligado=True)
        self.Timer = Timer(ligado=False)

    @classmethod
    def incrementa_contador(cls):
        cls.contador += 1
        
        
    def abrir_sinal(self):
      self.lampada_verde = Lampada(cor=VERDE,ligado=False)
      self.lampada_verde.acender()
      print(f"Sinal verde foi aberto!")
    
sem = Semaforo()

sem.abrir_sinal()








