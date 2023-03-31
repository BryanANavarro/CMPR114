# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #6

import random

def main():
	# Create a deck of cards
	deck = create_deck()

	# Get the number of cards to deal
	num_cards = 1

	
	player1Score = 0
	player2Score = 0
	
	while (True):
		# Deal the cards
		player1_card1, player1_Value1 = deal_cards(deck, num_cards)
		player2_card1, player2_Value1 = deal_cards(deck, num_cards)
		player1_card2, player1_Value2 = deal_cards(deck, num_cards)
		player2_card2, player2_Value2 = deal_cards(deck, num_cards)

		# If there are two aces in the first two cards, -10 from one ace
		player1Score = player1_Value1 + player1_Value2
		if 'Ace' in player1_card1 and player1_card2:
			player1Score - 10
		player2Score = player2_Value1 + player2_Value2
		if 'Ace' in player2_card1 and player2_card2:
			player2Score - 10

		if player1Score == 21:
			print(f"Player 1 wins with a score of {player1Score} with {player1_card1} and {player1_card2}")
			break
		if player2Score == 21:
			print(f"Player 2 wins with a score of {player2Score} with {player2_card1} and {player2_card2}")
			break

		while player1Score <= 21:
			print(f"\nPlayer 1 score is: {player1Score}")
			print(f"Player 2 score is: {player2Score}")
			hit_or_stay = input("Player 1, do you want to hit or stay? H - hit and S - stay: ")
			if hit_or_stay.lower() == 'h':
				player1_newCard, player1_newValue = deal_cards(deck, num_cards)
				player1Score += player1_newValue
				if player1Score > 21:
					if 'Ace' in player1_card1 or 'Ace' in player1_card2 or 'Ace' in player1_newCard:
						player1Score -= 10
					else:
						print(f"\nPlayer 1 busted with {player1Score}")
						print(f"Player 2 wins with {player2Score}")
						return
			elif hit_or_stay.lower() == 's':
				break

		while player2Score < 21 and player1Score <= 21:
			print(f"\nPlayer 1 score is: {player1Score}")
			print(f"Player 2 score is: {player2Score}")
			hit_or_stay = input("Player 2, do you want to hit or stay? H - hit and S - stay: ")
			if hit_or_stay.lower() == 'h':
				player2_newCard, player2_newValue = deal_cards(deck, num_cards)
				player2Score += player2_newValue
				if player2Score > 21:
					if 'Ace' in player2_card1 or 'Ace' in player2_card2 or 'Ace' in player2_newCard:
						player2Score -= 10
					else:
						print(f"\nPlayer 2 busted with {player2Score}")
						print(f"Player 1 wins with {player1Score}")
						return
			elif hit_or_stay.lower() == 's':
				break

		# All the different combinations of the game 
		if player1Score > player2Score and player1Score <= 21:
			print(f"\nPlayer 1 is the winner with {player1Score}!")
			break
		elif player1Score < player2Score and player2Score <= 21:
			print(f"\nPlayer 2 is the winner with {player2Score}!")
			break
		elif player1Score == player2Score:
			print(f"\nIt's a tie at {player1Score}")
			break
		elif player1Score > 21 and player2Score > 21:
			print(f"\nPlayer 1 and Player 2 busted!")
			break


# The create_deck function returns a dictionary
# representing a deck of cards
def create_deck():
	# Create a dictionary with each card and its value
	# stored as key-value pairs.
	# in this program, aces are worth 11
	deck = {'Ace of Spades':11, '2 of Spades' :2, '3 of Spades': 3,
		    '4 of Spades': 4,'5 of Spades': 5,'6 of Spades': 6,
		    '7 of Spades': 7,'8 of Spades': 8, '9 of Spades': 9,
			'10 of Spades': 10, 'Jack of Spades': 10,
			'Queen of Spades': 10, 'King of Spades': 10,
			
			'Ace of Hearts':11, '2 of Hearts' :2, '3 of Hearts': 3,
		    '4 of Hearts': 4,'5 of Hearts': 5,'6 of Hearts': 6,
		    '7 of Hearts': 7,'8 of Hearts': 8, '9 of Hearts': 9,
			'10 of Hearts': 10, 'Jack of Hearts': 10,
			'Queen of Hearts': 10, 'King of Hearts': 10,
			
			'Ace of Clubs':11, '2 of Clubs' :2, '3 of Clubs': 3,
		    '4 of Clubs': 4,'5 of Clubs': 5,'6 of Clubs': 6,
		    '7 of Clubs': 7,'8 of Clubs': 8, '9 of Clubs': 9,
			'10 of Clubs': 10, 'Jack of Clubs': 10,
			'Queen of Clubs': 10, 'King of Clubs': 10,
			
			'Ace of Diamonds':11, '2 of Diamonds' :2, '3 of Diamonds': 3,
		    '4 of Diamonds': 4,'5 of Diamonds': 5,'6 of Diamonds': 6,
		    '7 of Diamonds': 7,'8 of Diamonds': 8, '9 of Diamonds': 9,
			'10 of Diamonds': 10, 'Jack of Diamonds': 10,
			'Queen of Diamonds': 10, 'King of Diamonds': 10}
	# Return the deck
	return deck

# The deal_cards function deals a specified number of cards
# from the deck
def deal_cards(deck, number):
	# Initialize an accumulator for the hand value
	hand_value = 0

	# Make sure the number of cards to deal is not
	# greater than the number of cards in the deck.
	if number > len(deck):
		number = len(deck)

	# Deal the cards and accumulate their values.
	for count in range(number):
		card = random.choice(list(deck))
		hand_value = deck[card]

	# Display the value of the hand
	return card, hand_value

# Call the main function.
if __name__ == '__main__':
	main()