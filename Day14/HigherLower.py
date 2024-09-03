# Start of higher/lower game

import random
from data import data
from art import logo
from art import vs

score = 0
option_A = []
option_B = []

def setup():
    global data, option_A, option_B, temp_A
    print(logo)
    print(f"Your score {score}")
    if option_A == []:
        temp_A = random.choice(data)
        option_A.append(temp_A)
        data.remove(temp_A)
        list(option_A)
    temp_B = random.choice(data)
    option_B = []
    option_B.append(temp_B)
    data.remove(temp_B)
    list(option_B)
    if option_A == option_B:
        setup()
    print(f"Compare A: {option_A[0]["name"]}, a {option_A[0]["description"]}, from {option_A[0]["country"]}")
    print(vs)
    print(f"Compare B: {option_B[0]["name"]}, a {option_B[0]["description"]}, from {option_B[0]["country"]}")
    data.append(temp_A)
    data.append(temp_B)
    higher_lower()

def higher_lower():
    global score, option_A, option_B
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
        right_or_wrong = option_A[0]["follower_count"] > option_B[0]["follower_count"]
        if right_or_wrong == True:
            score += 1
            option_A = option_B
            setup()
        elif right_or_wrong == False:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
    elif answer == "b":
        wrong_or_right = option_B[0]["follower_count"] > option_A[0]["follower_count"]
        if wrong_or_right == True:
            score += 1
            option_A = option_B
            setup()
        elif wrong_or_right == False:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()

setup()