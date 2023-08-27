class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def get_imc(self,peso,altura:float):
        self.peso = peso
        self.altura = altura
        imc = peso / (altura * altura)
        print(f" o imc de é de {imc}")
        

anderson = Pessoa("anderson",19)
anderson.get_imc(70,1.70)
        