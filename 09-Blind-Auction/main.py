import os
from art import logo

print(logo)

bids = {}

# To clean screen
def clear_screen():
    os.system('cls')
    
# Get the max bid and bidder name
def winner_bid(bid_record):
	max = 0
	winner = ""
	for i in bid_record:
		if bid_record[i] > max:
			max = bid_record[i]
			winner = i
	print(f"The winner is {winner} for ${max} amount.")	


keep_bidding = True

while keep_bidding == True:
	name = input("What is your name? ").lower()
	bid = int(input("What's your bid? : $"))
	bidder = input("Are they any other bidders? Type 'Yes' or 'No': ").lower()
	# Adding new bids in bids dictionary
	bids[name] = bid
	clear_screen()
 
	if bidder != 'yes':
		keep_bidding = False
	# Call the function with bids arg. to get the winner
	winner_bid(bids)
	
