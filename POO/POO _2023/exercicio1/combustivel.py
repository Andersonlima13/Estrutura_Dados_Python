valor_total = 0
gasolina = 6
alcool = 5

class Bomba_combustivel:
  
  def __init__(self,litro,tipo_combustivel):
    self.litro = litro
    self.tipo_combustivel = tipo_combustivel
    

  def abastecer(self,litros,tipo_combustivel):
    if tipo_combustivel == gasolina:
      valor_total = gasolina * litros
      print(f" o valor a ser pago com gasolina é {valor_total} para {litros} litros")
    else:
      valor_total = alcool * litros
      print(f" o valor a ser pago com alcool é {valor_total} para {litros} litros")
    




carro1 = Bomba_combustivel(0,gasolina)
carro1.abastecer(30,gasolina)
print(carro1)