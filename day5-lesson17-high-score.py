# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

#find the highest number in list

highHeight = 0

for a in student_scores:
  if highHeight < a:
    highHeight = a

print(f"The highest score in the class is: {highHeight}")
