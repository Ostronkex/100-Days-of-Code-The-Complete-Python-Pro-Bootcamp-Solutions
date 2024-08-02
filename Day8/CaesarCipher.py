caesar = ["""     
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |  _________   | || |    _______   | || |      __      | || |  _______     | |
| |   .' ___  |  | || |     /  \     | || | |_   ___  |  | || |   /  ___  |  | || |     /  \     | || | |_   __ \    | |
| |  / .'   \_|  | || |    / /\ \    | || |   | |_  \_|  | || |  |  (__ \_|  | || |    / /\ \    | || |   | |__) |   | |
| |  | |         | || |   / ____ \   | || |   |  _|  _   | || |   '.___`-.   | || |   / ____ \   | || |   |  __ /    | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |  _| |___/ |  | || |  |`\____) |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
| |   `._____.'  | || ||____|  |____|| || | |_________|  | || |  |_______.'  | || ||____|  |____|| || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """]

cipher = [""" 
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     _____    | || |   ______     | || |  ____  ____  | || |  _________   | || |  _______     | |
| |   .' ___  |  | || |    |_   _|   | || |  |_   __ \   | || | |_   ||   _| | || | |_   ___  |  | || | |_   __ \    | |
| |  / .'   \_|  | || |      | |     | || |    | |__) |  | || |   | |__| |   | || |   | |_  \_|  | || |   | |__) |   | |
| |  | |         | || |      | |     | || |    |  ___/   | || |   |  __  |   | || |   |  _|  _   | || |   |  __ /    | |
| |  \ `.___.'\  | || |     _| |_    | || |   _| |_      | || |  _| |  | |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |   `._____.'  | || |    |_____|   | || |  |_____|     | || | |____||____| | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """]
print(caesar)
print(cipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def question():
    start_over = input("Would you like to encode/decode? Y/N, Yes/No ").lower()
    if start_over == "yes" or start_over == "y" :
        main()
    elif start_over == "no" or start_over == "n" :
         print("Piss off") 
    else: 
        print("Yes or no, how hard can it be?")
        question()

def main():
    global alphabet, direction, text_encode, text_decode, shift
    direction = input("Would you like to encode or decode?")
    if direction == "encode": # Om user input encode, se nedan
        text_encode = input("What word would you like to encode?")
        text_encode = list(text_encode)
        shift = int(input("Type the shift number:\n"))
        for position in range(len(text_encode)): # Iterera genom ett spann av 0 - längden på ordet som skall krypteras, tilldela variabel "position" värdet 0,1,2 etc
            letter = text_encode[position] # Tilldela variabel "letter" en bokstav i taget från det krypterade ordet, börja på index 0 och sluta på sista index i ordet. 
            a = alphabet.index(letter) + shift # Hämta indexet från listan alphabet motsvarande bokstaven "letter" + förskjutning motsvarande shift. Tilldela detta värde variabel a, detta kommer att vara en siffra motsvarande ordningen i alfabetet
            if a >= len(alphabet): # Om förskjutningen hamnar utanför list-intervallet, se nedad
                a -= len(alphabet) # Tilldelat värde genom förskjutning - längden på alfabetet. T.ex. Z med shift 5 hade fått index 30, här blir det 30 minus längden på alfabetet (26) = 4, index 4 är E, femte bokstaven i alfabetet
            swap = alphabet[a] # Variabel "swap" tilldelas en bokstav motsvarande index a i listan alphabet. Var a har just nu en siffra tilldelad
            text_encode[position] = swap # Index position i text_list byts ut mot bokstaven som swap tilldelades. Position har i första iterationen värde 0 så här byter vi först index 0 i ordet, sedan index 1 etc för varje ny iteration 
        text_encode = "".join(text_encode)
        print(f"Your encoded word is: {text_encode}")
        question()
    elif direction == "decode": # Om user input decode, exakt samma kod som ovan fast omvänd. Minus shift för att gå bakåt i alfabetet.
        for position in range(len(text_list)): 
            letter = text_list[position]
            a = alphabet.index(letter) - shift
            swap = alphabet[a]
            text_list[position] = swap
        text_list = "".join(text_list)
        print(f"Your decoded word is: {text_list}")

main()

# Arkiverad testkod, kanske kan använda något av detta senare(?), fungerar ej just nu
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
 
