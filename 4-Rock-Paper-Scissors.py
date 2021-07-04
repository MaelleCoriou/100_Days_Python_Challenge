import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gamer = int(input("What do you choose? \nType 0 for Rock \nType 1 for Paper \nType 2 for Scissors\n"))

computer = random.randint(0,2)

# List of the ascii variables to call
choice = [rock, paper, scissors]

# Print the index chosen
if gamer >= 0 and gamer <= 2:
  print(choice[gamer])
  print(f"computer chose :\n{choice[computer]}")
  if gamer == 0 and computer == 2:
    print("you win")
  elif gamer == 2 and computer == 1:
    print("You win")
  elif gamer == 1 and computer == 0:
    print("You win")
  elif gamer == computer:
    print("It's a draw")
  else:
    print("You lose")
else:
  print("You typed a wrong number")



# Other printing solution, without a list :

# if gamer == 0:
#   print(rock)
# elif gamer == 1:
#   print(paper)
# elif gamer == 2:
#   print(scissors)

# if computer == 0:
#   print(f"computer chose :\n{rock}")
# elif computer == 1:
#   print(f"computer chose :\n{paper}")
# elif computer == 2:
#   print(f"computer chose :\n{scissors}")

# if gamer == 0 and computer == 2:
#   print("you win")
# elif gamer == 2 and computer == 1:
#   print("You win")
# elif gamer == 1 and computer == 0:
#   print("You win")
# elif gamer == computer:
#   print("It's a draw")
# elif gamer > 2:
#   print("You typed a wrong number")
# else:
#   print("You lose")

