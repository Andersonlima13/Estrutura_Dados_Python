class Bomba_combustivel:
  valor_total = 0
  valor_gasolina = 6
  valor_alcool = 5
  def __init__(self,litro,combustivel=True):
    self.litro = litro
    

  def abastecer(self,litros,combustivel,valor_gasolina,valor_alcool):
    if combustivel == True:
      valor_total = valor_gasolina * litros
      print(f" o valor a ser pago com gasolina é {valor_total} para {litros} litros")
    valor_total = valor_alcool * litros
    print(f" o valor a ser pago com alcool é {valor_total} para {litros} litros")
    




carro1 = Bomba_combustivel()
carro1.abastecer(30,True)
print(carro1)