import os
import random
import hangman_art
import hangman_words
# from hangman_art import stages, logo
# from hangman_words import word_list

# Word chosen randomly
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# While end_of_game is false game isn't over
end_of_game = False

# 6 errors max 
lives = 6
# lives = len(stages) - 1

# All letter guessed
guessed = []

# Imported logo from hangman_art.py to print it at the start of the game.
print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# To clean screen
def clear_screen():
    os.system('cls')
    
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
        
    clear_screen()
    
    print(hangman_art.logo)
    
    # If the user entered a letter more than once
    guessed += guess
    count = guessed.count(guess)

    if guess in guessed :   
        if count > 1:
            print(f"You've already guessed the letter {guess}, try another one.")

    # ----- Angela's solution ----- #
    
    # if guess in display:
    #     print(f"You've already guessed {guess}.")  

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter not in chosen_word :
        lives -= 1
        print(f"The letter {guess} is not in the word. you lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all elements in the list, turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
