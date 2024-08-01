alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Konvertera input text till en lista för enkel index-hantering
text_list = list(text)

# Ändra varje bokstav i användarens ord
# En bokstav i taget flyttar X antal steg framåt i alfabetet beroende på vad man specificerat via input shift.
# T.ex. ord "abc" med shift 2 blir "cde"
if direction == "encode": # Om user input encode
  for position in range(len(text_list)): # Iterera genom ett spann av 0 - längden på ordet som skall krypteras, tilldela variabel "position" värdet 0,1,2 etc
    letter = text_list[position] # Tilldela variabel "letter" en bokstav i taget från det krypterade ordet, börja på index 0 och sluta på sista index i ordet
    a = alphabet.index(letter) + shift # Hämta indexet från listan alphabet motsvarande bokstaven "letter" + förskjutning motsvarande shift. Tilldela detta värde variabel a, detta kommer att vara en siffra motsvarande ordningen i alfabetet
    if a => len(alphabet): # Om förskjutningen hamnar utanför list-intervallet, se nedan
      a -= len(alphabet) # Tilldelat värde genom förskjutning - längden på alfabetet. T.ex. Z med shift 5 hade fått index 30, här blir det 30 minus längden på alfabetet (26) = 4, index 4 är E, femte bokstaven i alfabetet
    swap = alphabet[a] # Variabel "swap" tilldelas en bokstav motsvarande index a i listan alphabet. Var a har just nu en siffra tilldelad
    text_list[position] = swap # Index position i text_list byts ut mot bokstaven som swap tilldelades. Position har i första iterationen värde 0 så här byter vi först index 0 i ordet, sedan index 1 etc för varje ny iteration 
elif direction == "decode": # Kod för dekryptering när krypteringen fungerar bättre
  print("We don't support decoding")

print(text_list)

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
 
