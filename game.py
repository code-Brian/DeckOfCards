from classes.deck import Deck
from classes.player import Player

current_deck = Deck()
current_deck.shuffle_cards()
current_deck.show_cards(current_deck.shuffled_deck)

current_deck.clear_shuffled_deck()

# bicycle = Deck()

# bicycle.show_cards()  
