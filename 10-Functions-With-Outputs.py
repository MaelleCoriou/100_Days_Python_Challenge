# functions with outputs

# def format_name(f_name, l_name):
# 	formated_f = f_name.title()
# 	formated_l = l_name.title()
# 	return f"{formated_f} {formated_l}"

# formated_string = format_name("MAElle", "cOriOu")
# print(formated_string)

def format_name(f_name, l_name):
	if f_name == "" or l_name == "":
		# Exit the function if an output isn't given
		return "You didn't provide valid output."
	formated_f = f_name.title()
	formated_l = l_name.title()
	return f"{formated_f} {formated_l}"

# args are given with inputs	
print(format_name(input("What is you first name? "), input("What is your lastname? ")))