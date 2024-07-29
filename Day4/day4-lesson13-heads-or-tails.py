# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

cointoss = random.randint(0,1)
round(cointoss)

if cointoss == 0:
  print("Tails")
else:
  print("Heads")
