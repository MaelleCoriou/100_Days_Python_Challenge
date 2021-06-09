# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
count = 0

for height in student_heights:
  # Additionner chaque height et l'enregistrer dans la variable total_height
  total_height += height
  # Compter le nombre de mesures dans la liste et l'enregistrer dans la variable count
  count += 1
# Calcul de la moyenne
print(round(total_height / count))