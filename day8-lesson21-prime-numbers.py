def prime_checker(number):
    prime = True
    for _ in range(2, number):
        print(_)
        if number % _ == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

numCheck = int(input("What number would you like to check? "))
prime_checker(number=numCheck)