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
bidders = []
more_bidders = ""
acceptable_answers_y = ["yes", "y"]
acceptable_answers_n = ["no", "n"]
winner = {

}
temp = []



def main():
    global gavel
    print(gavel)
    print("Welcome to the silent auction!")
    setup()

def setup():
    global name, bid, numbers, bidders, more_bidders
    bidder = {
        "name": "",
        "bid": None
    }
    def my_name():
        bidder["name"] = input("What is your name? ")
        if bidder["name"].isalpha():
            pass
        else:
            print("Only letters allowed")
            my_name()
    my_name()
    def my_bid():
        bidder["bid"] = input("What is your bid? ")
        if bidder["bid"].isdigit():
            bidder["bid"] = int(bidder["bid"])
        else:
            print("Only numbers are allowed")
            my_bid()
    my_bid()
    bidders.append(dict(name = bidder["name"], bid = bidder["bid"]))
    def multiple_bidders():
        global more_bidders, acceptable_answers_y, acceptable_answers_n
        more_bidders = input("Any other bidders? ").lower()
        if more_bidders in acceptable_answers_y:
            print(f"\n" * 100)
            setup()
        elif more_bidders in acceptable_answers_n:
            print("Thanks for bidding")
            results()
        else:
            print("Invalid input")
            multiple_bidders()
    def results():
        global winner, bidders
        for _ in bidders:
            if _["bid"] >= _["bid"]:
                winner = dict(name = _["name"], bid = _["bid"])
        print(f"The winner is {winner["name"]} with a bid of {winner["bid"]}")
        exit()
    multiple_bidders()
main()
