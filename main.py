from prettytable import PrettyTable
import random

print("Welcome to the game of Rock, Paper and Scissors!!!")
print("Please tell me your name: ", end="")
userName = input()

print("Hello", userName, "! \nLets start the game")
print("Please enter the total no. of rounds you want to play: ", end="")
totalRounds = int(input())

# all possible values in the game
rpsList = ["Rock", "Paper", "Scissors"]

# initialize user and computer points
userPoints = 0
computerPoints = 0

# history list
userHistory = []
computerHistory = []
winnerHistory = []

while totalRounds > 0:
    print("Press:\n1. Rock\n2. Paper\n3. Scissor")
    userTurn = int(input())
    if userTurn not in range(1, 4):                 # to check if user enter correct input
        print("Incorrect option selected! Please enter the choice again")
        continue
    computerTurn = random.choice([1, 2, 3])

# update history list for user and computer
    computerHistory.append(rpsList[computerTurn - 1])
    userHistory.append(rpsList[userTurn - 1])

    if userTurn == computerTurn:                    # if both the party choose same value
        winnerHistory.append("Tie")
    elif (userTurn % 3) < (computerTurn % 3):       # using MOD operator to determine computer as the winner
        computerPoints += 1
        winnerHistory.append("Computer")
    else:                                           # when user wins
        userPoints += 1
        winnerHistory.append(userName)

    historyTable = PrettyTable(["Round No.", userName + " selected", "Computer selected", "Winner"])

    # add rows to the game history table
    for i in range(0, len(userHistory)):
        historyTable.add_row([i + 1, userHistory[i], computerHistory[i], winnerHistory[i]])

    print(historyTable)

    # Update total round counter
    totalRounds -= 1

print("Final points are as follows:\n", userName, ": ",userPoints, "\nComputer: ", computerPoints, sep="")
print("And the Winner is...")
if userPoints > computerPoints:
    print(userName)
elif userPoints < computerPoints:
    print("Computer")
else:
    print("No one! It's a Tie!")

#clearing table
historyTable.clear_rows()