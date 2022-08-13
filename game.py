from classes.deck import Deck
from classes.player import Player

bicycle = Deck()

bicycle.show_cards()

brian = Player(["Ace, 10 of spades"])

brian.hit().stay()