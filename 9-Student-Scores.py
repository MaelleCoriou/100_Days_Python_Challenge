student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO: Write your code below to add the grades to student_grades.👇

student_grades = {}

for score in student_scores:
	if student_scores[score] <= 70:
		student_grades[score] = "Fail"
	elif student_scores[score] > 70 and student_scores[score] <= 80:
		student_grades[score] = "Acceptable"
	elif student_scores[score] > 80 and student_scores[score] <= 90:
		student_grades[score] = "Exceeds Expectations"
	elif student_scores[score] > 90:
		student_grades[score] = "Outstanding"

## ------- Angela's code -------##

# for student in student_scores:
# 	score = student_grades[student]
# 	if score > 90:
# 		student_grades[student] = "Outstanding"
# 	elif score > 80:
# 		student_grades[student] = "Exceeds Expectations"
# 	elif score > 70:
# 		student_grades[student] = "Acceptable"
# 	else:
# 		student_grades[student] = "Failed"

# 🚨 Don't change the code below 👇
print(student_grades)





