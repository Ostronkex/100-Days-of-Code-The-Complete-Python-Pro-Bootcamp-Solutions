# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height = float(height)
weight = int(weight)

bmi = weight / height**2
bmi = int(bmi)
print(bmi)

