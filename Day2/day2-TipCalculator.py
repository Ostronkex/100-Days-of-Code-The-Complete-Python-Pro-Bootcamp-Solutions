print("Welcome to the tip calculator!") #Welcome message
bill = input("What was the total bill? $") #bill var asking for input in dollars
tip = input("How much tip would you like to give? %") #tip var asking for input on how much tip to give in %
tipSplit = input("How many people to split the bill?")


bill = float(bill) #Converting var bill from str to int
tip = int(tip) #Converting var tip from str to int
tipSplit = int(tipSplit) #Converting var tipSplit from str to int

totalTip = bill * (tip / 100) #Calculate tip based on input given in % and the total bill

billWithTip = (totalTip + bill) / tipSplit #Takes the tip and adds it to the bill, then divide by the number of people to split the bill

billWithTip = round(billWithTip, 2) #Round the total to two decimal points
billWithTip = str(billWithTip) #Converting var billWithTip to str in order to concatenate it in the final message

print(f"Each person should pay: ${billWithTip}") #Final message concatenating a str + the billWithTip and prints the result
