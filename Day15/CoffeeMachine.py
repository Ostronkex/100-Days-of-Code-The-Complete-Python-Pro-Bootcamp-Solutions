# Start of coffee machine

"""
1. Print report (resources left)
2. Check that resources are sufficient for chosen drink
3. Process coins (quarter, dime, nickles, pennies)
4. Check transaction successful
5. Make coffee and deduct resources from total, add coins to cash register

1. What would you like
2. Please insert coins
    2.1: How many quarters?
    2.2: How many dimes?
    2.3: How many nickles?
    2.4: How many pennies?
3. If coins not enough for drink, refund and abort
4. If coins are enough, calculate total coin input and return change based on cost of coffee
5. Give drink
"""

from CoffeeData import MENU
from CoffeeData import resources
import random