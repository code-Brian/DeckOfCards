from classes.deck import Deck
from classes.deck import Randomized_Deck

current_deck = Randomized_Deck()

class Player:

    players = []

    def __init__(self, name:str, ) -> None:
        self.name = name

    def hit(self, deck):
        self.hand.append(deck.pop())
        print("Player hit.")
        return self.hand
    
    def stay(self):
        print("Player stays")
        return self

