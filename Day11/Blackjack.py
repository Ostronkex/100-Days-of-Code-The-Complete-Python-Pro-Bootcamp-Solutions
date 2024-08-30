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
cards = [
    {
"H2": r"""  
.------.  
|2_  _ |  
|( \/ )|   
| \  / |   
|  \/ 2| 
'------'
""", "value": 2
    },
    {
"H3": """
.------.  
|3_  _ |  
|( \/ )|   
| \  / |   
|  \/ 3| 
'------'
""", "value": 3
    },
    {
"H4": """
.------.  
|4_  _ |  
|( \/ )|   
| \  / |   
|  \/ 4| 
'------'
""", "value": 4
    },
    {
"H5": """
.------.  
|5_  _ |  
|( \/ )|   
| \  / |   
|  \/ 5| 
'------'
""", "value": 5
    },
    {
"H6": """
.------.  
|6_  _ |  
|( \/ )|   
| \  / |   
|  \/ 6| 
'------'
""", "value": 6
    },
    {
"H7": """
.------.  
|7_  _ |  
|( \/ )|   
| \  / |   
|  \/ 7| 
'------'
""", "value": 7
    },
    {
"H8": """
.------.  
|8_  _ |  
|( \/ )|   
| \  / |   
|  \/ 8| 
'------'
""", "value": 8
    },
    {
"H9": """
.------.  
|9_  _ |  
|( \/ )|   
| \  / |   
|  \/ 9| 
'------'
""", "value": 9
    },
    {
"H10": """
.------.  
|10    |  
|( \/ )|   
| \  / |   
|  \/10| 
'------'
""", "value": 10
    },
    {
"HJ": """
.------.  
|J_  _ |  
|( \/ )|   
| \  / |   
|  \/ J| 
'------'
""", "value": 10
    },
    {
"HD": """
.------.  
|D_  _ |  
|( \/ )|   
| \  / |   
|  \/ D| 
'------'
""", "value": 10
    },
    {
"HK": """
.------.  
|K_  _ |  
|( \/ )|   
| \  / |   
|  \/ K| 
'------'
""", "value": 10
    },
    {
"HA": """
.------.  
|A_  _ |  
|( \/ )|   
| \  / |   
|  \/ A| 
'------'
""", "value": 11
    },
    {
"R2": """
.------.
|2 /\  |   
| /  \ |  
| \  / |  
|  \/ 2|  
'------'
""", "value": 2
    },
    {
"R3": """
.------.
|3 /\  |   
| /  \ |  
| \  / |  
|  \/ 3|  
'------'
""", "value": 3
    },
    {
"R4": """
.------.
|4 /\  |   
| /  \ |  
| \  / |  
|  \/ 4|  
'------'
""", "value": 4
    },
    {
"R5": """
.------.
|5 /\  |   
| /  \ |  
| \  / |  
|  \/ 5|  
'------'
""", "value": 5
    },
    {
"R6": """
.------.
|6 /\  |   
| /  \ |  
| \  / |  
|  \/ 6|  
'------'
""", "value": 6
    },
    {
"R7": """
.------.
|7 /\  |   
| /  \ |  
| \  / |  
|  \/ 7|  
'------'
""", "value": 7
    },
    {
"R8": """
.------.
|8 /\  |   
| /  \ |  
| \  / |  
|  \/ 8|  
'------'
""", "value": 8
    },
    {
"R9": """
.------.
|9 /\  |   
| /  \ |  
| \  / |  
|  \/ 9|  
'------'
""", "value": 9
    },
    {
"R10": """
.------.
|10/\  |   
| /  \ |  
| \  / |  
|  \/10|  
'------'
""", "value": 10
    },
    {
"RJ": """
.------.
|J /\  |   
| /  \ |  
| \  / |  
|  \/ J|  
'------'
""", "value": 10
    },
    {
"RD": """
.------.
|D /\  |   
| /  \ |  
| \  / |  
|  \/ D|  
'------'
""", "value": 10
    },
    {
"RK": """
.------.
|K /\  |   
| /  \ |  
| \  / |  
|  \/ K|  
'------'
""", "value": 10
    },
    {
"RA": """
.------.
|A /\  |   
| /  \ |  
| \  / |  
|  \/ A|  
'------'
""", "value": 11
    },
    {
"K2": """
.------.
|2 _   |
| ( )  |
|(_x_) |
|  I  2|
'------'
""", "value": 2
    },
    {
"K3": """
.------.
|3 _   |
| ( )  |
|(_x_) |
|  I  3|
'------'
""", "value": 3
    },
    {
"K4": """
.------.
|4 _   |
| ( )  |
|(_x_) |
|  I  4|
'------'
""", "value": 4
    },
    {
"K5": """
.------.
|5 _   |
| ( )  |
|(_x_) |
|  I  5|
'------'
""", "value": 5
    },
    {
"K6": """
.------.
|6 _   |
| ( )  |
|(_x_) |
|  I  6|
'------'
""", "value": 6
    },
    {
"K7": """
.------.
|7 _   |
| ( )  |
|(_x_) |
|  I  7|
'------'
""", "value": 7
    },
    {
"K8": """
.------.
|8 _   |
| ( )  |
|(_x_) |
|  I  8|
'------'
""", "value": 8
    },
    {
"K9": """
.------.
|9 _   |
| ( )  |
|(_x_) |
|  I  9|
'------'
""", "value": 9
    },
    {
"K10": """
.------.
|10_   |
| ( )  |
|(_x_) |
|  I 10|
'------'
""", "value": 10
    },
    {
"KJ": """
.------.
|J _   |
| ( )  |
|(_x_) |
|  I  J|
'------'
""", "value": 10
    },
    {
"KD": """
.------.
|D _   |
| ( )  |
|(_x_) |
|  I  D|
'------'
""", "value": 10
    },
    {
"KK": """
.------.
|K _   |
| ( )  |
|(_x_) |
|  I  K|
'------'
""", "value": 10
    },
    {
"KA": """
.------.
|A _   |
| ( )  |
|(_x_) |
|  I  A|
'------'
""", "value": 11
    },
    {
"S2": """
.------.
|2 .   |
| / \  |
|(_,_) |
|  I  2|
'------'
""", "value": 2
    },
    {
"S3": """
.------.
|3 .   |
| / \  |
|(_,_) |
|  I  3|
'------'
""", "value": 3
    },
    {
"S4": """
.------.
|4 .   |
| / \  |
|(_,_) |
|  I  4|
'------'
""", "value": 4
    },
    {
"S5": """
.------.
|5 .   |
| / \  |
|(_,_) |
|  I  5|
'------'
""", "value": 5
    },
    {
"S6": """
.------.
|6 .   |
| / \  |
|(_,_) |
|  I  6|
'------'
""", "value": 6
    },
    {
"S7": """
.------.
|7 .   |
| / \  |
|(_,_) |
|  I  7|
'------'
""", "value": 7
    },
    {
"S8": """
.------.
|8 .   |
| / \  |
|(_,_) |
|  I  8|
'------'
""", "value": 8
    },
    {
"S9": """
.------.
|9 .   |
| / \  |
|(_,_) |
|  I  9|
'------'
""", "value": 9
    },
    {
"S10": """
.------.
|10.   |
| / \  |
|(_,_) |
|  I 10|
'------'
""", "value": 10
    },
    {
"SJ": """
.------.
|J .   |
| / \  |
|(_,_) |
|  I  J|
'------'
""", "value": 10
    },
    {
"SD": """
.------.
|D .   |
| / \  |
|(_,_) |
|  I  D|
'------'
""", "value": 10,
    },
    {
"SK": """
.------.
|K .   |
| / \  |
|(_,_) |
|  I  K|
'------'
""", "value": 10,
    },
    {
"SA": """
.------.
|A .   |
| / \  |
|(_,_) |
|  I  A|
'------'
""", "value": 11,
    }
    ]

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