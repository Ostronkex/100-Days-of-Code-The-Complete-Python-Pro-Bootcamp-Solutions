rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock, paper, scissors]

choice = input("Rock, Paper or Scissors?")
choice = choice.lower()
computer_choice = 0

if choice == "rock" or "paper" or "scissors":
  computer_choice = random.randint(1,3)
  if choice == "rock" and computer_choice == 1:
    print(f"You pick rock \n {rps[0]} \n Computer picks rock {rps[0]} \n It's a draw!")
  elif choice == "rock" and computer_choice == 2:
    print(f"You pick rock \n {rps[0]} \n Computer picks paper\n {rps[1]} \n You lose!")
  elif choice == "rock" and computer_choice == 3:
    print(f"You pick rock \n {rps[0]} \n Computer picks scissors \n {rps[2]} \n You win!")
  elif choice == "paper" and computer_choice == 1:
    print(f"You pick paper \n {rps[1]} \n Computer picks rock \n {rps[0]} \n You win!")
  elif choice == "paper" and computer_choice == 2:
    print(f"You pick paper \n {rps[1]} \n Computer picks paper \n {rps[1]} \n It's a draw!")
  elif choice == "paper" and computer_choice == 3:
    print(f"You pick paper \n {rps[1]} \n Computer picks scissors \n {rps[2]} \n You lose!")
  elif choice == "scissors" and computer_choice == 1:
    print(f"You pick scissors \n {rps[2]} \n Computer picks rock {rps[0]} \n You lose!")
  elif choice == "scissors" and computer_choice == 2:
    print(f"You pick scissors \n {rps[2]} \n Computer picks paper \n {rps[1]} \n You win!")
  elif choice == "paper" and computer_choice == 3:
    print(f"You pick scissors \n {rps[2]} \n Computer picks scissors \n {rps[2]} \n It's a draw!")
  elif choice != "rock" or  "paper" or "scissors":
    print("Please pick a legal weapon")
