#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []
hard_psw = ""

for num_letter in range(1, nr_letters +1):
  password += letters[random.randint(0, len(letters)-1)]
  # password += random.choice(letters)
  # password.append(random.choice(letters))

for num_symbol in range(1, nr_symbols +1):
  password += symbols[random.randint(0, len(symbols)-1)]
  # password += random.choice(symbols)

for num_num in range(1, nr_numbers +1):
  password += numbers[random.randint(0, len(numbers)-1)]
  # password += random.choice(numbers)

# Mélanger la liste password
random.shuffle(password)

# imprimer une liste en chaîne de caractères
print("Your password is :")
for e in password:
   print(e, end='')
  
# Autre solution pour print liste en chaine de caractères:
# password_print = ""
# for e in password:
#   password_print += e
# print(f"Your password is: {password_print}")