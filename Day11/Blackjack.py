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


cards_values = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
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
index11 = 0
computer_index11 = 0
card1_test = ""
card2_test = ""
tempcard = 0 
computer_tempcard = 0


def start():
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if answer == "y":
        blackjack_game()
    elif answer == "n":
        exit()
    else:
        print("Invalid entry, try again retard")
        start()

def question(): # Ask for another card
    global my_answer, my_total, computer_total, index11, tempcard
    my_answer = input("Would you like another card? ").lower()
    if my_answer == "yes" or my_answer == "y":
        print("\n")
        my_total = 0
        computer_total = 0
        tempcard = random.choice(cards_values)

        my_cards.append(tempcard)
        cards_values.remove(tempcard)
        tempcard = 0
        for _ in my_cards:
            my_total += _
        print(f"Your cards {my_cards}, current score {my_total}")
        print(f"Computers cards {computers_cards}")
        if my_total > 21 and 11 in my_cards: # Ace logic converting 11 to 1 if above 21
            my_total = 0
            print("Over 21, converting ace to 1")
            index11 = my_cards.index(11)
            my_cards[index11] = 1
            print(my_cards)
            for _ in my_cards:
                my_total += _
        print(f"Your total is {my_total}")
        if my_total == 21: # Blackjack conditional
            print("Blackjack!")
            again()
        elif my_total > 21: # Lose conditional
            print("Bust, you lose!")
            again()
        for _ in computers_cards:
            computer_total += _
        print(f"Computers total is {computer_total}")
    elif my_answer == "no" or my_answer == "n": # Generate cards for the computer if I stop
        print("\n")
        computer_total = 0
        computer_blackjack()
    else:
        print("Invalid input, try again")
        question()
    
def computer_blackjack():
    global computer_total, computer_index11, computer_tempcard
    while computer_total <= my_total: # Give cards to the computer as long as its total is lower than mine and under 21
        computer_total = 0
        computer_tempcard = random.choice(cards_values)
        cards_values.remove(computer_tempcard)
        computers_cards.append(computer_tempcard)
        print(computers_cards)
        for _ in computers_cards:
            computer_total += _
        if computer_total > 21 and 11 in computers_cards: # Ace logic converting 11 to 1 if total is above 21
            computer_total = 0
            print("Over 21, converting ace to 1")
            computer_index11 = computers_cards.index(11)
            computers_cards[computer_index11] = 1
            print(f"Computer's cards: {computers_cards}")
            for _ in computers_cards:
                computer_total += _
        print(f"Computers total is {computer_total}")
        if computer_total > my_total and computer_total < 22:
            print("Computer wins!")
            again()
        elif computer_total > 21: 
            print("Computer bust. You win!")
            again()
    
def blackjack_game(): # Blackjack game
    global my_cards, card1, card2, computers_card1, computers_card2, my_total, computer_total, my_answer
    print(blackjack)

    # Initial two random cards
    card1 = random.choice(cards_values) 
    cards_values.remove(card1)
    card2 = random.choice(cards_values)
    cards_values.remove(card2)

    my_cards.append(card1)
    my_cards.append(card2)
    my_total = card1 + card2
    print(f"Your cards: {my_cards}, current score: {my_total}")
    my_total = 0
    computers_card1 = random.choice(cards_values)
    cards_values.remove(computers_card1)
    computers_cards.append(computers_card1)
    print(f"Computers first card {computers_cards}")
    for _ in my_cards:
        my_total += _
    if my_total == 21:
        print("Blackjack!")
        again()
    for _ in computers_cards:
        computer_total += _
    if computer_total == 21:
        print("Computer wins!")
        again()
    while my_total < 21:
        question()
 
def again(): # Play again y/n
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

""" These cards were supposed to replace the numbers in my_cards with pretty ASCII-art. 
    However the connection between a random generated value, the index it represented and the card chosen were too difficult to figure out at my current level.
    I'm sure I can solve it with some ugly solution such as grabbing a unique index from a list of numbers/cards (see list cards[] below), match that index so the corresponding card and
    assing a value to each card. My mind was spinning just thinking about it. I will potentially return to this in the future once I learn more concepts. For the actual project, Day 11
    is considered done according to the course material.
"""

""" cards = {
    'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'H10': 10,
    'HJ': 10, 'HD': 10, 'HK': 10, 'HA': 11,
    'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10,
    'RJ': 10, 'RD': 10, 'RK': 10, 'RA': 11,
    'K2': 2, 'K3': 3, 'K4': 4, 'K5': 5, 'K6': 6, 'K7': 7, 'K8': 8, 'K9': 9, 'K10': 10,
    'KJ': 10, 'KD': 10, 'KK': 10, 'KA': 11,
    'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10,
    'SJ': 10, 'SD': 10, 'SK': 10, 'SA': 11
} """

my_list = [
"""  
.------.  
|2_  _ |  
|( \/ )|   
| \  / |   
|  \/ 2| 
'------'
""",
"""
.------.  
|3_  _ |  
|( \/ )|   
| \  / |   
|  \/ 3| 
'------'
""",
"""
.------.  
|4_  _ |  
|( \/ )|   
| \  / |   
|  \/ 4| 
'------'
""",
"""
.------.  
|5_  _ |  
|( \/ )|   
| \  / |   
|  \/ 5| 
'------'
""",
"""
.------.  
|6_  _ |  
|( \/ )|   
| \  / |   
|  \/ 6| 
'------'
""",
"""
.------.  
|7_  _ |  
|( \/ )|   
| \  / |   
|  \/ 7| 
'------'
""",
"""
.------.  
|8_  _ |  
|( \/ )|   
| \  / |   
|  \/ 8| 
'------'
"""
"""
.------.  
|9_  _ |  
|( \/ )|   
| \  / |   
|  \/ 9| 
'------'
""",
"""
.------.  
|10    |  
|( \/ )|   
| \  / |   
|  \/10| 
'------'
""",
"""
.------.  
|J_  _ |  
|( \/ )|   
| \  / |   
|  \/ J| 
'------'
""",
"""
.------.  
|D_  _ |  
|( \/ )|   
| \  / |   
|  \/ D| 
'------'
""",
"""
.------.  
|K_  _ |  
|( \/ )|   
| \  / |   
|  \/ K| 
'------'
""",
"""
.------.  
|A_  _ |  
|( \/ )|   
| \  / |   
|  \/ A| 
'------'
""",
"""
.------.
|2 /\  |   
| /  \ |  
| \  / |  
|  \/ 2|  
'------'
""",
"""
.------.
|3 /\  |   
| /  \ |  
| \  / |  
|  \/ 3|  
'------'
""",
"""
.------.
|4 /\  |   
| /  \ |  
| \  / |  
|  \/ 4|  
'------'
""",
"""
.------.
|5 /\  |   
| /  \ |  
| \  / |  
|  \/ 5|  
'------'
""",
"""
.------.
|6 /\  |   
| /  \ |  
| \  / |  
|  \/ 6|  
'------'
""",
"""
.------.
|7 /\  |   
| /  \ |  
| \  / |  
|  \/ 7|  
'------'
""",
"""
.------.
|8 /\  |   
| /  \ |  
| \  / |  
|  \/ 8|  
'------'
""",
"""
.------.
|9 /\  |   
| /  \ |  
| \  / |  
|  \/ 9|  
'------'
""",
"""
.------.
|10/\  |   
| /  \ |  
| \  / |  
|  \/10|  
'------'
""",
"""
.------.
|J /\  |   
| /  \ |  
| \  / |  
|  \/ J|  
'------'
""",
"""
.------.
|D /\  |   
| /  \ |  
| \  / |  
|  \/ D|  
'------'
""",
 """
.------.
|K /\  |   
| /  \ |  
| \  / |  
|  \/ K|  
'------'
""",
"""
.------.
|A /\  |   
| /  \ |  
| \  / |  
|  \/ A|  
'------'
""",
"""
.------.
|2 _   |
| ( )  |
|(_x_) |
|  I  2|
'------'
""",
"""
.------.
|3 _   |
| ( )  |
|(_x_) |
|  I  3|
'------'
""",
"""
.------.
|4 _   |
| ( )  |
|(_x_) |
|  I  4|
'------'
""",
"""
.------.
|5 _   |
| ( )  |
|(_x_) |
|  I  5|
'------'
""",
"""
.------.
|6 _   |
| ( )  |
|(_x_) |
|  I  6|
'------'
""",
"""
.------.
|7 _   |
| ( )  |
|(_x_) |
|  I  7|
'------'
""",
"""
.------.
|8 _   |
| ( )  |
|(_x_) |
|  I  8|
'------'
""",
"""
.------.
|9 _   |
| ( )  |
|(_x_) |
|  I  9|
'------'
""",
"""
.------.
|10_   |
| ( )  |
|(_x_) |
|  I 10|
'------'
""",
"""
.------.
|J _   |
| ( )  |
|(_x_) |
|  I  J|
'------'
""",
 """
.------.
|D _   |
| ( )  |
|(_x_) |
|  I  D|
'------'
""",
"""
.------.
|K _   |
| ( )  |
|(_x_) |
|  I  K|
'------'
""",
"""
.------.
|A _   |
| ( )  |
|(_x_) |
|  I  A|
'------'
""",
"""
.------.
|2 .   |
| / \  |
|(_,_) |
|  I  2|
'------'
""",
"""
.------.
|3 .   |
| / \  |
|(_,_) |
|  I  3|
'------'
""",
"""
.------.
|4 .   |
| / \  |
|(_,_) |
|  I  4|
'------'
""",
"""
.------.
|5 .   |
| / \  |
|(_,_) |
|  I  5|
'------'
""",
"""
.------.
|6 .   |
| / \  |
|(_,_) |
|  I  6|
'------'
""",
"""
.------.
|7 .   |
| / \  |
|(_,_) |
|  I  7|
'------'
""",
"""
.------.
|8 .   |
| / \  |
|(_,_) |
|  I  8|
'------'
""",
"""
.------.
|9 .   |
| / \  |
|(_,_) |
|  I  9|
'------'
""",
"""
.------.
|10.   |
| / \  |
|(_,_) |
|  I 10|
'------'
""",
"""
.------.
|J .   |
| / \  |
|(_,_) |
|  I  J|
'------'
""",
"""
.------.
|D .   |
| / \  |
|(_,_) |
|  I  D|
'------'
""",
"""
.------.
|K .   |
| / \  |
|(_,_) |
|  I  K|
'------'
""",
"""
.------.
|A .   |
| / \  |
|(_,_) |
|  I  A|
'------'
"""
]

cards_image = [
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