class Player:
    def __init__(self, hand):
        self.hand = hand

    def hit(self):
        print("Player requests a card")
        return self
    
    def stay(self):
        print("Player stays")
        return self

class Dealer(Player):
    super(Player)