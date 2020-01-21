import random

x = random.randint(1, 99)
guess, n = 0, 0

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99.")
print("Type 'exit' to end the game.")
print("Good luck!")
print(' ')

while int(n) != x:
    print("What's your guess between 1 and 99?")
    n = input(">> ")
    if n == "exit":
        print("Goodbye!")
        exit(1)
    try:
        int(n)
    except:
        print("That's not a number.")
    else:
        if int(n) > x:
            print("Too high!")
        elif int(n) < x:
            print("Too low!")
    guess += 1

if x == 42:
    print("The answer to the ultimate question of life, the universe ....")
print("Congratulations, you've got it!")
print("You won in {} attempts!".format(guess))
