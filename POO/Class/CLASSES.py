class Pessoa:
    def __init__(self, nome , idade, comendo=False, falando=False ):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando 
        
    def falar(self,assunto):
        if self.comendo:
            print(f"{self.nome} Não podendo falar enquanto come")
            return
        if self.falando:
            print(f"{self.nome} Já está falando")
            return
        print(f"{self.nome} está falando sobre {assunto} ")
        self.falando = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo")
            return
        print(f"{self.nome} parou de comer ")
        self.comendo = False        