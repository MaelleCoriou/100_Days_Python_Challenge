from art import logo

print(logo)

# Add
def add(n1, n2):
	return n1 + n2

# Multiply
def multiply(n1, n2):
	return n1 * n2

# Sustract
def substract(n1, n2):
	return n1 - n2

# Divide
def divide(n1, n2):
	return n1 / n2
	
operations = {
	"+": add,
	"*": multiply,
	"-": substract,
	"/": divide,
	}

num1 = int(input("What's the first number?: "))
for i in operations:
	print(i)
operation_symbol = input("Pick an operation from the list above.")
num2 = int(input("What's the second number?: "))

# Function getting related operation function to symbol chosen
calulation_function = operations[operation_symbol]
# Saving calculation result to a variable
answer = calulation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
