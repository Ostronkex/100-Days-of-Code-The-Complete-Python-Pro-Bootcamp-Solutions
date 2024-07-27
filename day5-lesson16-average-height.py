# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

totHeight = 0

for height in student_heights:
  totHeight += height

numHeight = 0

for numStud in student_heights:
  numHeight += 1

avHeight = totHeight / numHeight
avHeight = round(avHeight)
print(f"total height = {totHeight}")
print(f"number of students = {numHeight}")
print(f"average height = {avHeight}")
