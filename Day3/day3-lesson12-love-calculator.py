print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t_count = name1.count("t") + name2.count("t")
r_count = name1.count("r") + name2.count("r")
u_count = name1.count("u") + name2.count("u")
e_count = name1.count("e") + name2.count("e")
l_count = name1.count("l") + name2.count("l")
o_count = name1.count("o") + name2.count("o")
v_count = name1.count("v") + name2.count("v")

trueCount = str(t_count + r_count + u_count + e_count)
loveCount = str(l_count + o_count + v_count + e_count)

totalCount = trueCount + loveCount
totalCount = int(totalCount)

if totalCount < 10 or totalCount > 90:
  print(f"Your score is {totalCount}, you go together like coke and mentos.")
elif totalCount >= 40 and totalCount <= 50:
  print(f"Your score is {totalCount}, you are alright together.")
else:
  print(f"Your score is {totalCount}.")




     
