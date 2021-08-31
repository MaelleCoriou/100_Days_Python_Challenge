# # Data types can be set up from the beginning likewise:
# age: int
# height: float
# name: str

# data type input and expected data type output of a function can be set up
# (age: int) -> bool
def police_check(age: int) -> bool:
    """ age = int, function returns boolean """
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(12))

if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine")