# Start of silent auction

gavel = """                        
    ___________
    \\         /
     )_______(
     |       |_.-._,.---------.,_.-._
     |       | | |               | | ''-.
     |       |_| |_             _| |_..-'
     |_______| '-' `'---------'` '-'
     )       (
    /_________\\
    `'-------'`
  .-------------.
 /_______________\\
"""

name = ""
bid = 0
numbers = [0,1,2,3,4,5,6,7,8,9]

def main():
    global gavel
    print(gavel)
    print("Welcome to the silent auction!")
    setup()

def setup():
    global name, bid, numbers
    bidder = {
        "name": "",
        "bid": None
    }
    def my_name():
        bidder["name"] = input("What is your name? ")
        if isinstance(bidder["name"], str):
            pass
        else:
            print("Only letters allowed")
            my_name()
    def my_bid():
        bidder["bid"] = input("What is your bid? ")
        if bidder["bid"].isdigit():
            bidder["bid"] = int(bidder["bid"])
        else:
            print("Only numbers are allowed")
            my_bid()
            print(bidder)
main()

# Archived code for now, might be useful later
""" if bidder["bid"] in numbers:
    bidder["bid"] = int(bidder["bid"])
    pass
else:
    print("Only numbers are allowed")
    setup()
    print(f"You bid {bidder["bid"]}")
    bidder["name"] = input("What is your name? ")
    if isinstance(bidder[name], str):
        pass
    else:
        print("Only letters are allowed, start over")
        setup()
    print(bidder["name"])

setup() """

