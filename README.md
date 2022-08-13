# DeckOfCards
This is a bonus assignment for Coding Dojo's OOP.

You can read about Blackjack's rules here: https://bicyclecards.com/how-to-play/blackjack/

I'm going to be using this README as a running checklist while I implement features and get my code ironed out. My plan is eventually to polish this README
and have it solely explain how to play my game in the terminal.

First Goal:
Create a Player class that has the following attributes and methods:
attributes:

hand - player gets dealt a hand each round by a Dealer. My initial thought is that Dealer would be a great use case for inheritance, 
since Dealers can do everything a player can do, but Dealers have a special role in controlling the round, collecting/cashing out bets, giving
each player a 'hand' or two cards, etc. 

bank - the amount that each player starts with, and is either collected from or paid to depending on whether or not the player wins or loses each round.

methods:
bet() - declare and deduct your bet at the start of each round from each players Bank
hit()
stand()

