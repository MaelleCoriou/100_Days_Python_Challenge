import pandas as pd

# Goal: Get the phonetic alphabet for any word entered by a user

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Nato with Df
user_word = input("Enter your word: ").upper()
for letter in user_word:
    for (index, row) in data.iterrows():
        if letter == row.letter:
            print(row.letter, row.code)

# Nato with Dic
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}
user_word = input("Enter your word: ").upper()
Nato_list = [nato_dic[letter] for letter in user_word]
print(Nato_list)
