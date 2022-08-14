from classes.deck import Deck

class Player:

    players = []

    def __init__(self, name:str, deck:list) -> None:
        self.name = name
        self.deck = deck

    def hit(self, deck):
        self.hand.append(deck.pop())
        print("Player hit.")
        return self.hand
    
    def stay(self):
        print("Player stays")
        return self

