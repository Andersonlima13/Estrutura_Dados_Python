class Animal:
    def __init__(self,tipo,idade,nome):
        self.tipo = tipo
        self.idade = idade
        self.nome = nome



#gato herda a classe animal

class Gato(Animal):
# PS :  atributos sempre devem iniciar-se com letras minusculas
    def __init__(self,nome,cor,idade,comendo=False,dormindo=True):
        self.tipo = "felino"
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.comendo = comendo  
        self.dormindo = dormindo
    
    def comer(self,alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo {alimento} no al mosso")
            return
        print(f" {self.nome} vai comer {alimento} no al mosso ")
        self.comendo = True
        
    def dormir(self):
        if self.comendo:
            print(f"{self.nome} está al mossando, não é hora de dormir")
            return
        print(f" {self.nome} está indo dormir")
        self.dormindo = True

    

    
g1 = Gato("japodhi_almossar_da_silva","branco","2")
g2 = Gato("aumosso","preto","1")
g1.comer("ração")
g1.dormir()


