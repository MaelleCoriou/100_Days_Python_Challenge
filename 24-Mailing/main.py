#TODO: Create a letter using starting_letter.txt 

with open("Input/Letters/starting_letter.txt") as f:
    letter = f.read()
    print(letter)

with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()
    print(names)

for name in names:
    guest = name.strip()
    new_letter = letter.replace("[name]", guest)
    with open("Output/ReadyToSend/Invitation_for_"+guest+".txt", mode="w") as f:
        f.write(new_letter)

# Angela's code:
# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
#
