import random

logo = """
   ___                       _____ _                 _                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

answer = random.randint(1, 100)

def guess_the_number():
    lives = 0
    guess = ""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Invalid input, try again")
        guess_the_number()
    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number")
        if lives == 0:
            print("You died. GGWP")
            print(f"The correct answer was {answer}")
            exit()
        guess = int(input("Make a guess: "))
        if guess < answer:
            lives -= 1
            print("Too low, guess again")
        elif guess > answer:
            lives -= 1
            print("Too high, guess again")
        elif guess == answer:
            print("You win!")
            exit()
        else:
            print("Invalid input, try again")

guess_the_number()