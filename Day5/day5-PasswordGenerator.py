#Initial code in the forked Replit from "100 Days of Code: The Complete Python Pro Bootcamp - Day 5: Password Generator"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#My code starting
import random

#Placeholder variable for the generated password
password_list = []

#For loop with a range of 0 to the number the user picks. Iterating through the letters list and generating a random character from it and then append (add) it to the password_list
for ltrs in range(0, nr_letters):
    password_list.append(random.choice(letters))

#Same as above witht the range of 0 to the number the user picks in the symbols input. Generating from the symbols list and add it to the password_list
for smbls in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

#Same as above, generate from the numbers list and add it to the password_list
for nmbrs in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

#Shuffles the list (password_list) to make it seem more random
random.shuffle(password_list)

#Run join() on the password list to join all the indexes together and form a string
password_list = "".join(password_list)
#Prints the final result
print(f"Your generated password is: {password_list}")
