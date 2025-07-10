from random import randint 
play = True
again = input("Would you like to play again? Yes or No.")
if again == "Yes": 
    play == True
if again == "No":
    play = False
while play == True:
    com_guess = randint(1,3)
    p_guess = int(input("Choose 1 for rock, 2 for paper, and 3 for scissors."))
    if com_guess == 3 and p_guess == 1:
        print("I chose scissors. You won!!!")
    elif com_guess == 2 and p_guess == 3:
        print("I chose paper. You won!!!")
    elif com_guess == 1 and p_guess == 2:
        print("I chose rock. You won!!!") 
    elif com_guess == 1 and p_guess == 3:
        print("I chose rock. You lost.")
    elif com_guess == 3 and p_guess == 2:
        print("I chose scissors. You lost.")
    elif com_guess == 2 and p_guess == 1:
        print("I chose paper. You lost.")
    else:
        print("We tied.")
    again = input("Would you like to play again? Yes or No.")
    if again == "No":
        play = False