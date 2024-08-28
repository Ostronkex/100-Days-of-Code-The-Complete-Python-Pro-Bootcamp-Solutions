# Start of Day 10 - Calculator

calculator_text = """
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
 """
calculator = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

print(calculator_text)

# Placeholder variables

temp = 0
total = 0
question = ""
reply = ""
operators = ["+", "-", "*", "/"]

def keep_going():
    question = input(f"Would you like to keep counting with {total}? yes/y or no/n: ").lower()
    if question == "yes" or question == "y":
        main()
    else: 
        print("Thank you for calculating with us today! Now fuck off")
        exit

def main():
    global temp, total, question, reply
    if total == 0:
        total = int(input("what number would you like to calculate? "))
    else:
        None
    print(temp)
    print("+")
    print("-")
    print("*")
    print("/")
    reply = input("What operator? ")
    if reply not in operators:
        print("Not a valid operator, try again retard")
        main()
    elif reply == "+":
        total += int(input("What number would you like to add? "))
        print(total)
        temp = 0
        keep_going()
    elif reply == "-":
        total -= int(input("What number would you like to subtract? "))
        print(total)
        temp = 0
        keep_going()
    elif reply == "*":
        total *= int(input("What number would you like to multiply with? "))
        print(total)
        temp = 0
        keep_going()
    elif reply == "/":
        total /= int(input("What number would you like to divide with? "))
        print(total)
        temp = 0
        keep_going()
main()
