import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

answer = random.randint(1, 100)
easy_lives = 10
hard_lives = 5

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()

def easy():
    global answer, easy_lives
    print(f"You have {easy_lives} attempts remaining to guess the number")
    if easy_lives == 0:
        print("You died. GGWP")
        print(f"The correct answer was {answer}")
        exit()
    guess = int(input("Make a guess: "))
    if guess < answer:
        easy_lives -= 1
        print("Too low.")
        print("Guess again.")
        easy()
    elif guess > answer:
        easy_lives -= 1
        print("Too high.")
        print("Guess again.")
        easy()
    elif guess == answer:
        print("You win!")
        exit()
    else:
        print("Invalid input, try again")
        easy()

def hard():
    global answer, hard_lives
    print(f"You have {hard_lives} attempts remaining to guess the number")
    if hard_lives == 0:
        print("You died. GGWP")
        print(f"The correct answer was {answer}")
        exit()
    guess = int(input("Make a guess: "))
    if guess < answer:
        hard_lives -= 1
        print("Too low.")
        print("Guess again.")
        hard()
    elif guess > answer:
        hard_lives -= 1
        print("Too high.")
        print("Guess again.")
        hard()
    elif guess == answer:
        print("You win!")
        exit()
    else:
        print("Invalid input, try again")
        hard()

guess_the_number()