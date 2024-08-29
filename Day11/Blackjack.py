# Start of Blackjack


""" 1. Print welcome screen with ascii art - Check
2. Generate two cards for the player between 2 and 10, wait with the ace for now which is considered 1 and 11 depending on the outcome - Partially check, add ace logic
3. Show the computers first card - Check
4. Ask if user wants another card or not - Check
    4.1. If yes, give another card and add to total, computer stays at same card. - Check
    4.2. If no, let computer hit and check the outcome - Check
5. The computer only receives cards when you stop hitting to try to surpass your score. - Check
    5.1. Make sure to add a conditional statement to let the computer hit if his score is lower than yours. - Check
6. Print win/lose and then if the user wants to play again. - Check """ 

import random

blackjack = r""" 
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/            
"""
my_cards = []
my_total = 0
card1 = 0
card2 = 0
computers_cards = []
computers_card1 = 0
computers_card2 = 0
computer_total = 0
my_answer = ""
reply = ""


def start():
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if answer == "y":
        blackjack_game()
    elif answer == "n":
        exit()
    else:
        print("Invalid entry, try again retard")
        start()

def question(): # Fråga om ett till kort
    global my_answer, my_total, computer_total
    my_answer = input("Would you like another card? ").lower()
    if my_answer == "yes" or my_answer == "y":
        print("\n")
        my_total = 0
        computer_total = 0
        my_cards.append(random.randint(2, 11))
        print(f"Your cards {my_cards}")
        print(f"Computers cards {computers_cards}")
        for _ in my_cards:
            my_total += _
        if 11 in my_cards and my_total > 21:
            my_total -= 10
        print(f"Your total is {my_total}")
        if my_total == 21:
            print("Blackjack!")
            exit()
        elif my_total > 21:
            print("Bust, you lose!")
            again()
        for _ in computers_cards:
            computer_total += _
        print(f"Computers total is {computer_total}")
    elif my_answer == "no" or my_answer == "n":
        print("\n")
        computer_total = 0
        computer_blackjack()
    else:
        print("Invalid input, try again")
        question()
    
def computer_blackjack():
    global computer_total
    while computer_total <= my_total:
        computer_total = 0
        computers_cards.append(random.randint(2, 11))
        print(computers_cards)
        for _ in computers_cards:
            computer_total += _
        if computer_total > 21 and 11 in computers_cards:
            computer_total -= 10
        print(f"Computers total is {computer_total}")
        if computer_total > my_total and computer_total < 22:
            print("Computer wins!")
            again()
        elif computer_total > 21: 
            print("Computer bust. You win!")
            again()
    
def blackjack_game(): # Blackjack spel
    global my_cards, card1, card2, computers_card1, computers_card2, my_total, computer_total, my_answer
    print(blackjack)
    card1 = random.randint(2, 11)
    card2 = random.randint(2, 11)
    my_cards.append(card1)
    my_cards.append(card2)
    print(f"Your cards {my_cards}")
    computers_card1 = random.randint(2, 11)
    computers_card2 = random.randint(2, 11)
    computers_cards.append(computers_card1)
    computers_cards.append(computers_card2)
    print(f"Computers cards {computers_cards}")
    for _ in my_cards:
        my_total += _
    print(f"Your total is {my_total}")
    if my_total == 21:
        print("Blackjack!")
        again()
    for _ in computers_cards:
        computer_total += _
    print(f"Computers total is {computer_total}")
    while my_total < 21:
        question()

def again():
    global reply, my_cards, my_total, computers_cards, computer_total
    reply = input("Would you like to play again? yes/y or no/n ").lower()
    if reply == "yes" or reply == "y":
        my_cards = []
        my_total = 0
        computers_cards = []
        computer_total = 0
        start()
    elif reply == "no" or reply == "n":
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid input, try again")
        again()
start()



