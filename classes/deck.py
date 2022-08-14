from . import card
import random

class Deck:

    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        self.shuffled_deck = []
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(cls, deck):
        print("show_cards was called....")
        for card in deck:
            if(card not in deck):
                print("There are no cards in this deck...")
            else:
                card.card_info()

    def get_random_card( self ):
        self.random_card = random.randint(0,51)
        return self.random_card

    def shuffle_cards( self ):
        i = 0
        while i < 52:
            i += 1
            current_card = self.cards[self.get_random_card()]

            if (current_card in self.shuffled_deck):

                card_picked = True
                while card_picked:
                    new_card = self.cards[self.get_random_card()]
                    if (new_card not in self.shuffled_deck):
                        self.shuffled_deck.append(new_card)
                        break
                    else:
                        continue
            else:
                self.shuffled_deck.append(current_card)
        return self.shuffled_deck

    def clear_shuffled_deck(self):
        print("clearing shuffled deck...")
        for i in range(0, len(self.shuffled_deck)):
            self.shuffled_deck.pop(i)
        return self.shuffled_deck

