#Number Guessing Game Objectives:
import random
from art import logo
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def compare(player_guess, result):
    if player_guess > result:
        return "Too high."
    elif player_guess < result:
        return "Too low."
    else:
        return f"You got it! The answer was {result}"
        

def level_range(level):
    if level == "hard":
        return 5
    elif level == "easy":
        return 10


def game_guess():

    print(logo)

    level = input("""Welcome to the Number Guessing Game!

	I'm thinking of a number between 1 and 100.
	
    Choose a difficulty. 

            Type 'easy' or 'hard': 
    
    """)

    guess = random.randint(1,100)
    print(guess)
    make_guess = 0
    
    while make_guess != guess:
        for e in range(level_range(level)):
            print(f"You have {level_range(level)-e} attempts remaining to guess the number.")
            make_guess = int(input("Make a guess: "))
            print(compare(make_guess, guess))
            if make_guess == guess:
                return
        if make_guess != guess:
            print("You've run out of guesses, you lose.")
            return
        else:
            return

game_guess()