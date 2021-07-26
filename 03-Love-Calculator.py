# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
name = name1 + name2

count_true=['t','r','u', 'e']

def true(name, count_true):
  count=0
  for i in name:
      if str(i) in count_true:
          count+=1
  return count
true_count = true(name, count_true)

count_love = ['l', 'o', 'v', 'e']

def love(name, count_love) :
  count = 0
  for i in name:
      if str(i) in count_love:
          count+=1
  return count
love_count = love(name, count_love)

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")