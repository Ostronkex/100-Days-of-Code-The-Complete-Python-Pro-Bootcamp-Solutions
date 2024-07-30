# Write your code below this line 👇
n = int(input())
number = n

for num in range(1, number):
  if number % num == 0 and number % 1 == 0:
    print("Prime")
  else: 
    print("Not prime")
  
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
