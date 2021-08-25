import pandas as pd

# Goal: Get the phonetic alphabet for any word entered by a user

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Nato with Df


def generate_phonetic_df():
    user_word = input("Enter your word: ").upper()
    # Exception if input entered is not in alphabet
    if 'A' <= user_word <= 'Z':
        for letter in user_word:
            for (index, row) in data.iterrows():
                if letter == row.letter:
                    print(row.letter, row.code)
    else:
        print(f"Sorry {user_word} is not valid, only letters in the alphabet")
        # Ask the word again
        generate_phonetic_df()


generate_phonetic_df()

# Nato with Dic
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic_dic():
    user_word = input("Enter your word: ").upper()
    try:
        nato_list = [nato_dic[letter] for letter in user_word]
    except KeyError as message_error:
        # if key doesn't exists in dic
        print(f"Sorry, {message_error} not valid, only letters in the alphabet")
        generate_phonetic_dic()
    else:
        print(nato_list)


generate_phonetic_dic()
