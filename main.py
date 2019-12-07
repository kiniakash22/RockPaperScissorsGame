import random

print("Welcome to the game of Rock, Paper and Scissors!!!")
print("Please tell me your name ^_^")
userName = input()

print("Hello", userName, "! \nLets start the game")
print("Please enter the total no. of rounds you want to play: ", end="")
totalRounds = int(input())

# all possible values in the game
rpsList = ["Rock", "Paper", "Scissors"]

# initialize user and computer points
userPoints = 0
computerPoints = 0

while totalRounds > 0:
    print("Press:\n1. Rock\n2. Paper\n3. Scissor")
    userTurn = int(input())
    if userTurn not in range(1, 4):                 # to check if user enter correct input
        print("Incorrect option selected! Please enter the choice again")
        continue
    computerTurn = random.choice([1, 2, 3])
    print("Computer Choose: ", rpsList[computerTurn - 1])
    print("You Choose: ", rpsList[userTurn - 1])

    if userTurn == computerTurn:                    # if both the party choose same value
        print("It's a TIE!s")
    elif (userTurn % 3) < (computerTurn % 3):       # using MOD operator to determine computer as the winner
        computerPoints += 1
        print("I WON!!!")
    else:                                           # when user wins
        userPoints += 1
        print("You WON", userName, "!")

    # Update total round counter
    totalRounds -= 1
