print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#'You're at a crossroad. Where do you want to go? Type "left" or "right"'
#'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
#"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
#"It's a room full of fire. Game Over."
#"You found the treasure! You Win!"
#You enter a room of beasts. Game Over."
#"You chose a door that doesn't exist. Game Over."
#"You get attacked by an angry trout. Game Over."
#"You fell into a hole. Game Over."

direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
direction = direction.lower()

if direction != "left":
  print("You fall into a hole. GAME OVER")
else:
  print("You go left")
  direction = input("Swim or wait?")
  if direction != "wait":
    print("You swim")
    print("You are attacked by a trout") 
  else:
    direction = input("Which door? Red, Blue or Yellow?")
  if direction == "red":
    print("You go through the red door")
    print("Burned by fire")
  if direction== "blue":
    print("You go through the blue door")
    print("Eaten by beast")
  if direction == "yellow":
    print("You go through the yellow door")
    print("You Win!")
  else:
    print("GAME OVER")
  
