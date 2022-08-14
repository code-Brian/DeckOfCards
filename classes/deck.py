from . import card
import random

class Deck:

    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

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

    def show_cards(self):
        for card in self.cards:
            card.card_info()

# this subclass will hold our randomized deck each round
class Randomized_Deck(Deck):

    def __init__( self ):
        super().__init__()
        self.shuffled_deck = []
    
    def get_random_card( self ):
        self.random_card = random.randint(0,51)
        return self.random_card

    # create a function that shuffles the list of cards in the deck
    # define the function which will use a card deck as a param
    def shuffle_cards( self ):
        # create a list which holds the shuffled cards
        # create a while loop that runs until the length of the shuffled deck is 52 unique cards
        i = 0
        while i < 52:
            i += 1
            current_card = self.cards[self.get_random_card()]
            print(f'Random card picked was: {current_card}\n')

            if (current_card in self.shuffled_deck):
                print(f"{current_card} is already in the shuffled deck.\n")

                card_picked = True
                while card_picked:
                    print(f'Picking a different card..."')
                    new_card = self.cards[self.get_random_card()]
                    print(f'card value is: {new_card}\n')
                    if (new_card not in self.shuffled_deck):
                        self.shuffled_deck.append(new_card)
                        print(f'{new_card} added to shuffled deck via inner while loop/if statement')
                        break
                    else:
                        print(f'{new_card} was already in the shuffled deck.')
                        continue
            else:
                self.shuffled_deck.append(current_card)
                print(f"{current_card} added to the shuffled deck via outer else statement")
        return self.shuffled_deck

    def show_cards(self):
        for card in self.shuffled_deck:
            card.card_info()



