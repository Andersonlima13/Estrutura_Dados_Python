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
    self.esta_ligado = ligado


  def trocar_cor(self,cor):
      self.cor = cor
      if cor == VERDE:
          print(f" sinal {VERDE} sinal está aberto")  



class Semaforo:
    contador = 0
    def __init__(self):
        self.incrementa_contador()
        self.lampada_verde = Lampada(cor=VERDE, ligada=False)
        self.lampada_amarela = Lampada(cor=AMARELO, ligada=False)
        self.lampada_vermelha = Lampada(cor=VERMELHO, ligada=True)
        self.Timer = Timer(ligado=False)

    @classmethod
    def incrementa_contador(cls):
        cls.contador += 1
        
    
   

