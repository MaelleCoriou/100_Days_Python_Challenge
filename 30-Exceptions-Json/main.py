# Error examples
#
# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()
#
# # KeyError
# dic = {"key": "value"}
# value = dic["non_existent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# # TypeError
# text = "abcd"
# print(text + 5)

# Handling exceptions

# try:
# something that might cause exception
# except:
# do this if there is an exception
# else:
# do this if there were no exceptions
# finally:
# do this no matter what happens

# FileNotFound
try:
    file = open("a_file.txt")
    dic = {"key": "value"}
    print(dic["key"])
except FileNotFoundError:
    # Create a file if doesn't exists
    file = open("a_file.txt", "w")
    file.write("Something")
# except KeyError:
#     print("that key doesn't exist")
except KeyError as error_message:
    print(f"The {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    # Raising an error no matter what with message, will crash the code
    # raise TypeError("This is an error I made up.")

# Raise my own error
# BMI calculator

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# ------------------ Exercise 1 ----------------------

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# ------------------ Exercise 2 ----------------------

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # If no Likes, likes = 0
        # total_likes += 0
        pass

print(total_likes)