
#Metodos especiales en python

print("Representa un juego estandar de cartas")
class Card(object):#Herencia
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):#Constructor
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs' ,'Diamonds' ,'Hearts' ,'Spades']#listas
    rank_names = [None, 'Ace' ,'2' , '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        #Retorna los valores pasados como parametros
        return ' %s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])

    #metodo especial para comparar
    def __cmp__(self, other):
        # check the suits
        if self.suit > other. suit: return 1
        if self.suit < other. suit: return -1
        # suits are the same... chec k ra nks
        if self.rank > other. rank: return 1
        if self.rank < other. rank: return -1
        # ranks are the same... it' s a tie
        return 0

card1 = Card(2, 11)
#retornara Jack of Hearts 
print(card1)#usa el metodo especial __str__() para representar el objeto

#objeto para comparar
card2=Card(2,11)
#Al compararlo con card1 retornara 0 porque son iguales
r=card1.__cmp__(card2)
print("Resultado de comparar card1 con card 2, son iguales: ",r)

#objeto de Card 3
card3=Card(3,12)
r=card1.__cmp__(card3)
print("Resultado de comparar card1 con card3, negativo card1<card3: ",r)
           

