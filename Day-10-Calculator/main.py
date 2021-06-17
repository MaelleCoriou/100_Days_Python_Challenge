# Calculator
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
	print(logo)

	num1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)

	Keep_calculating = True

	while Keep_calculating == True:
		operation_symbol = input("Pick an operation: ") 
		num2 = float(input("What's the next number?: "))

		# Function getting related operation function to symbol chosen
		calculation_function = operations[operation_symbol]

		# Saving calculation result to a variable
		answer = calculation_function(num1, num2)

		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. \n").lower() == "y":
			# Changing the num1 output and calculation to the new result to keep on calculating
			num1 = answer
		else:
			Keep_calculating = False
			# Calling the function itself to restart the calculator
			calculator()


calculator()
	




