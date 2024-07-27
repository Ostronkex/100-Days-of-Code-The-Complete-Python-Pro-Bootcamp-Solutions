target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

totalEven = 0

for number in range(2, target + 1):
  if number % 2 == 0:
    totalEven += number

print(totalEven)
