from game_data import data
from art import logo, vs
import random
import os


def random_choice():
    return random.choice(data)


def clear_screen():
    """To clean screen"""
    os.system('cls')


def info_celebrity(celebrity):
    """Get the name / description / country from a dic and print the info. celebriy : dic to print"""
    celebrity_name = celebrity["name"]
    celebrity_description = celebrity["description"]
    celebrity_country = celebrity["country"]
    return f'{celebrity_name}, a {celebrity_description}, from {celebrity_country}'


def compare(answer, followers_A, followers_B):
    """Gets the gamer answer and compare it to the followers' amount between A and B celebrity. Returns True or False."""
    if answer == "a" and followers_A > followers_B:
        return True
    elif answer == "b" and followers_B > followers_A:
        return True
    else :
        return False
    
    ## 2 other options :

    # if followers_A > followers_B:
    ## True if the answer is A
    #   return answer == "a"
    # else:
    ## False if the answer is B
    #   return answer == "b"

    # if followers_A > followers_B:
    #   if answer == "a"
    #       return True
    #   else:
    #       return False
        

print(logo)


def higher_lower():
    points = 0
    game = True

    celebrity_A = random_choice()
    celebrity_B = random_choice()

    while game:
        # Pick a celebrity randomly in data dic
        # Results B becomes result A when guess on B is right
        celebrity_A = celebrity_B
        celebrity_B = random_choice()

        # To avoid same matches
        while celebrity_A == celebrity_B:
            celebrity_B = random_choice()

        # Print celebrity A info using function
        print(f"Compare A {info_celebrity(celebrity_A)}")

        print(vs)

        # Print celebrity B info using function
        print(f"Against B {info_celebrity(celebrity_B)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Compare the followers count
        count_A = celebrity_A["follower_count"]
        count_B = celebrity_B["follower_count"]

        # Print results
        check = compare(guess, count_A, count_B)

        clear_screen()

        print(logo)

        # Score track and results print
        if check:
            points += 1
            print(f"You're right! Current score: {points}")
        else :
            game = False
            print(f"Sorry, that's wrong. Final score: {points}")
            replay = input("Do you want to play again ? Y or N : ").lower()
            clear_screen()
            
            if replay == "y":
                print(logo)
                higher_lower()
higher_lower()