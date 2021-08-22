numbers = [1, 2, 3]

# Loop in a list and create a new list
new_numbers_list = []
for n in numbers:
    new_num = n + 1
    new_numbers_list.append(new_num)
print("new_numbers_list =", new_numbers_list)

# List comprehension arguments
# new_list = [new_item for item in list]

# List comprehension with a list
new_numbers = [n + 1 for n in numbers]
print("numbers list =", numbers)
print("numbers list =", new_numbers)

# List comprehension with a string
name = "Maëlle"
list_letters = [letter for letter in name]
print("list_letters =", list_letters)

# List comprehension with a range
list_multiply = [num * 2 for num in range(1, 5)]
print("list_multiply range() = ", list_multiply)

# List comprehension with condition
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
long_name_caps = [name.upper() for name in names if len(name) > 4]
print("short_name =", short_name)
print("long_name_caps =", long_name_caps)

# Exercise squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print("squared_numbers =", squared_numbers)

# Exercise even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print("result =", result)

# Exercise list comprehension with 2 files
import pandas as pd

file1 = pd.read_csv("file1.txt", header=None)
file2 = pd.read_csv("file2.txt", header=None)
file1 = file1[0].tolist()
file2 = file2[0].tolist()

result_2 = [num for num in file1 if num in file2]
print(result_2)
print(type(result_2[0]))

## Angela's code
with open("file1.txt", encoding="UTF8") as f:
    file1 = f.readlines()
with open("file2.txt", encoding="UTF8") as f:
    file2 = f.readlines()
result = [int(num) for num in file1 if num in file2]
print(result)

# Dictionary comprehension
# new_dic = {new_key:new_value for item in list}
# new_dic = {new_key:new_value for (key, value) in dic.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in names}
print("New_dictionary =", students_score)
passed_students = {student: score for (student, score) in students_score.items() if score > 50}
print("New_dictionary with condition =", passed_students)

# Exercise Dic comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print("Count letters of each word:", result)

# Exercise Dic comprehension
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: ((temp* 9/5) + 32) for (day, temp) in weather_c.items()}
print("Dic with Celsius converted to Fahrenheit:", weather_f)

# Iterate over Pandas
student_dic = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [60, 56, 80, 90, 45, 78]
}
# Looping through dictionary
for (key, value) in student_dic.items():
    print(key)
    print(value)

# Looping with pandas
student_df = pd.DataFrame(student_dic)

# Loop through df
for (key, value) in student_df.items():
    print(key)
    print(value)

# Loop through df rows
for (index, row) in student_df.iterrows():
    #print(index)
    # pandas series object:
    #print(row)
    # get value in specific column
    #print(row.student)
    # get row with condition
    if row.student == "Alex":
        print(row.score)

# Dictionary comprehension with pandas to create a new dic and loop through df
# new_dic = {new_key: new_value for (index, row) in df.iterrows() if test}

