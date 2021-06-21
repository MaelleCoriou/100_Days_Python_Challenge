############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def somme(liste):
    total = 0
    for i in liste:
        total = total + i
    return total

def player(hits):
	player_cards = []
	for e in range(0,hits):
		player_cards.append(random.choice(cards))
	return player_cards

def dealer(hits):
	dealer_cards = []
	for e in range(0,hits):
		dealer_cards.append(random.choice(cards))
	return dealer_cards


def black_jack():
	player_cards = []
	total_player = 0
	dealer_cards = []
	total_dealer = 0
	game = True

	while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower() == 'y':

		print(logo)

		for e in range(2):
			player_cards.append(random.choice(cards))
			dealer_cards.append(random.choice(cards))
		total_player = somme(player_cards)
		total_dealer = somme(dealer_cards)

		print(f"Your cards: {player_cards}\nYour current score: {total_player}")
		print(f"Computer's first card: {dealer_cards[0]}")
		while game == True:
			while input("Type 'y' to get another card, type 'n' to pass:").lower() == 'y':
				player_cards.append(random.choice(cards))
				dealer_cards.append(random.choice(cards))
				total_player = somme(player_cards)
				total_dealer = somme(dealer_cards)

				if total_player >= 21 and player_cards[-1] == 11:
					player_cards[-1] = 1
					total_player = somme(player_cards)
					print(f"Your cards: {player_cards}\nYour current score: {total_player}")
					print(f"Computer's first card: {dealer_cards[0]}")
				elif total_player <= 21:
					print(f"Your cards: {player_cards}\nYour current score: {total_player}")
					print(f"Computer's first card: {dealer_cards[0]}")
				elif total_player > 21:
					print('You went over. You lose 😤')
					print(f"Your final hand: {player_cards}\nYour final score score: {total_player}")
					print(f"Computer's final hand: {dealer_cards}, final score {total_dealer}")
					game = False	
					black_jack()
			game = False
			if total_player > 21:
				print('You went over. You lose 😤')
				print(f"Your final hand: {player_cards}\nYour final score score: {total_player}")
				print(f"Computer's final hand: {dealer_cards}, final score {total_dealer}")
				game = False
				black_jack()
			elif total_player == total_dealer:
				print("Paw!")
				print(f"Your final hand: {player_cards}\nYour final score score: {total_player}")
				print(f"Computer's final hand: {dealer_cards}, final score {total_dealer}")
				black_jack()
			elif total_dealer > 21 :
				print('You win!')
				print(f"Your final hand: {player_cards}\nYour final score score: {total_player}")
				print(f"Computer's final hand: {dealer_cards}, final score {total_dealer}")
				game = False
				black_jack()
			elif total_dealer <= 21 and total_player > total_dealer:
				print("You win!")
				print(f"Your final hand: {player_cards}\nYour final score score: {total_player}")
				print(f"Computer's final hand: {dealer_cards}, final score {total_dealer}")
				black_jack()
		black_jack()

black_jack()