alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Konvertera input text till en lista för enkel index-hantering
text_list = list(text)

# Ändra varje bokstav i användarens ord
# En bokstav i taget flyttar X antal steg framåt i alfabetet beroende på vad man specificerat via input shift.
# T.ex. ord "abc" med shift 2 blir "cde"
if direction == "encode":
  for position in range(len(text_list)):
    letter = text_list[position]
    a = alphabet.index(letter) + shift
    swap = alphabet[a]
    text_list[position] = swap
elif direction == "decode":
  print("We don't support decoding")

print(text_list)

# Kanske kan använda något av detta senare(?)
""""for _ in text:
  for pos in range(len(text_list)):
    x = alphabet.index(_)
    if direction == "encode":
      x += shift
      print(x)
      swap = alphabet[x]
      position = len(text)
      print(swap)
      text_list[pos] = swap

position = len(text_list)
while position > len(text_list):
  for pos in range(len(text_list)):
    print(pos)
    letter = text_list[pos]
    text_list[pos] = swap

print(text_list)"""


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
 
