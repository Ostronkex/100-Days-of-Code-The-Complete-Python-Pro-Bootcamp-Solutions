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

print("Welcome to Caesar Cipher!")

direction = ""
text_encode = ""
text_decode = ""
shift = 0
encoded_word = ""
decoded_word = ""

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
    global alphabet, direction, text_encode, text_decode, shift, encoded_word, decoded_word
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:.\n")
    if direction == "encode": # Om user input encode, se nedan
        text_encode = input("Type your message:\n")
        if text_encode.isalpha():
            pass
        else:
            print("Only letters are allowed!")
            main()
        text_encode = list(text_encode)
        shift = (input("Type the shift number:\n"))
        if shift.isdigit():
            shift = int(shift)
        else:
            print("Only numbers are allowed!")
            main()
        for position in range(len(text_encode)): # Iterera genom ett spann av 0 - längden på ordet som skall krypteras, tilldela variabel "position" värdet 0,1,2 etc
            letter = text_encode[position] # Tilldela variabel "letter" en bokstav i taget från det krypterade ordet, börja på index 0 och sluta på sista index i ordet. 
            a = alphabet.index(letter) + shift # Hämta indexet från listan alphabet motsvarande bokstaven "letter" + förskjutning motsvarande shift. Tilldela detta värde variabel a, detta kommer att vara en siffra motsvarande ordningen i alfabetet
            if a >= len(alphabet): # Om förskjutningen hamnar utanför list-intervallet, se nedan
                a -= len(alphabet) # Tilldelat värde genom förskjutning - längden på alfabetet. T.ex. Z med shift 5 hade fått index 30, här blir det 30 minus längden på alfabetet (26) = 4, index 4 är E, femte bokstaven i alfabetet
            swap = alphabet[a] # Variabel "swap" tilldelas en bokstav motsvarande index a i listan alphabet. Var a har just nu en siffra tilldelad
            text_encode[position] = swap # Index position i text_list byts ut mot bokstaven som swap tilldelades. Position har i första iterationen värde 0 så här byter vi först index 0 i ordet, sedan index 1 etc för varje ny iteration 
        encoded_word = "".join(text_encode)
        print(f"Your encoded word is: {encoded_word}")
        question()
    elif direction == "decode": # Om user input decode, exakt samma kod som ovan fast omvänd. Minus shift för att gå bakåt i alfabetet samt att variablerna har andra namn specifikt för dekryptering
        text_decode = input("What word would you like to encode?")
        text_decode = list(text_decode)
        shift = int(input("Type the shift number:\n"))
        for position in range(len(text_decode)): 
            letter = text_decode[position] 
            a = alphabet.index(letter) - shift 
            if a >= len(alphabet): 
                a -= len(alphabet) 
            swap = alphabet[a] 
            text_decode[position] = swap 
        decoded_word = "".join(text_decode)
        print(f"Your encoded word is: {decoded_word}")
        question()
    else:
        print("Invalid input")
        main()
main()
 
