import random
from enum import Enum

class Naipe(Enum):
    OUROS = 1
    PAUS = 2
    COPAS = 3
    ESPADAS = 4

class Carta:
    AS = 1
    VALETE = 11
    RAINHA = 12
    REI = 13
    
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
        self.nome = self._get_nome()

    def _get_nome(self):
        match self.valor:
            case 1:
                return "Ás"
            case x if 2 <= x <= 10:
                return str(self.valor)
            case 11:
                return "Valete"
            case 12:
                return "Rainha"
            case 13:
                return "Rei"
            case _:
                raise ValueError("valor inválido")
            
    def __str__(self):
        return f'{self.nome} de {self.naipe.name.title()}'
    
    def __repr__(self):
        return f'Carta({self})'
    
    def __lt__(self, outra_carta: 'Carta') -> bool:
        return self.valor < outra_carta.valor
    
    def __eq__(self, outra_carta: 'Carta') -> bool:
        return self.valor == outra_carta.valor

class Baralho:
    
    def __init__(self):
        self._criar_cartas()
        self._embaralhar()
    
    def __len__(self):
        return len(self.cartas)
    
    def _criar_cartas(self):
        self.cartas = []
        for naipe in Naipe:
            for valor in range(1, 14):
                self.cartas.append(
                    Carta(valor=valor, naipe=naipe)
                )
    
    def _embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, *jogadores):
        quantidade = len(self) // len(jogadores)
        for i in range(len(jogadores)):
            jogadores[i].adicionar_cartas( self.cartas[i * quantidade: i * quantidade + 1] )
            
            
        
        
        
        




class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.deck = []

    def __repr__(self):
        return f'Jogador({self.nome})'
    
    def adicionar_cartas(self, *cartas):
        print(cartas)
        self.deck.extend(cartas)

    def adicionar_carta(self, carta: Carta):
        self.deck.append(carta)



b = Baralho()
j1 = Jogador("Rodrigo")
j2 = Jogador("Pinheiro")
j3 = Jogador("Marques")
b.distribuir(j1, j2, j3)