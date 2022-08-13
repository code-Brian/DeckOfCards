# DeckOfCards
This is a bonus assignment for Coding Dojo's OOP.

You can read about Blackjack's rules here: https://bicyclecards.com/how-to-play/blackjack/

I'm going to be using this README as a running checklist while I implement features and get my code ironed out. My plan is eventually to polish this README
and have it solely explain how to play my game in the terminal.

First Goal:
Create a Player class that has the following attributes and methods:
attributes:

players - a list of each instance of player created in each game. This can be used as a class attribute/method to cycle through each player
and have them perform an action.

  hand - player gets dealt a hand each round by a Dealer. My initial thought is that Dealer would be a great use case for inheritance, 
  since Dealers can do everything a player can do, but Dealers have a special role in controlling the round, collecting/cashing out bets, giving
  each player a 'hand' or two cards, etc.
  
  down_card - the face-down card that is only known to the player.
  face_card - the face-up card that is dealt.

  bank - the amount that each player starts with, and is either collected from or paid to depending on whether or not the player wins or loses each round.

methods:
  bet() - declare and deduct your bet at the start of each round from each players Bank
  hit() - if player indicates they'd like another card, they will receive the next card in the deck.
  stand() - if player would like to keep their current score, they will not take another card
  split() - if a player is dealt a pair of the same suit/number, give them the option to split each card into a new hand
  cut() - the player selected by the dealer cuts the deck in half.
  
Second Goal: 
Make an inherited child class of player that is the dealer for the game
attributes:
  dealer_hand - dealer gets two cards, both face down. 
  
methods:
  round_begin() - deals two cards for each player in the game, one face-down, the other, face-up.
  dealer_play() - dealers face-down card is turned face-up.
  deal() - dealer hits or stands depending player request/input
  
Third Goal:
Create a Blackjack_deck class that is a child of the deck class. It needs the following features:

attributes:
  shuffled_deck - a list variable that is a shuffled version of self.cards[]. 

Fourth Goal: 
Create a game class that runs the game

attributes:
  
methods: 
  play() - dictate the behavior of each class in the round.
  the dealer deals each player a card, based upon player hands, the players either hit or stay, and the dealer
  resolves bets - either paying or collecting bets depending on bust, natural, or blackjack conditions, etc. I will flesh this out more
  once I get a better idea of what all I need.
  
  # create a while loop that constantly plays rounds based upon whether or not a player wants to continue, or has won or lost.
  # 
  
