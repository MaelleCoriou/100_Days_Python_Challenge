from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	max = len(alphabet)

	# if shift entered is greater than the alphabet list
	if shift_amount > max:
		shift_amount = shift_amount %26
	
	# get index reversed for decode
	if cipher_direction == "decode":
		shift_amount *= -1

	# get new letter from new position
	for char in start_text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			# get symbols int 
			end_text += char		
	print(f"Here's the {cipher_direction}d result: {end_text}")
	

print(logo)

game = True

while game == True:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
	start = input("Do you want to restart Cipher? 'Yes' or 'No': \n")

	if start == "yes":
		game = True
	else:
		game = False
print("Goodbye!")