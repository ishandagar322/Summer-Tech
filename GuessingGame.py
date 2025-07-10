from random import randint
number = randint(0,100)
guess = int(input("Guess a number: "))
while guess != number: 
    if guess > number: 
        print("Your guess is too high.")
        guess = int(input("Guess again."))
    if guess < number: 
        print("Your guess is too low.")
        guess = int(input("Guess again."))
print("You got it right!")