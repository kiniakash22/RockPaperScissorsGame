from prettytable import PrettyTable
import random

computerAPoints = 0
computerBPoints = 0

historyTable = PrettyTable()


# all possible values in the game
rpsList = ["Rock", "Paper", "Scissors"]
# winner list mapping
winnerList = ["Tie", "Computer A", "Computer B"]

winnerHistory = []
winnerEntireHistory = []
computerAEntireHistory = []
computerBEntireHistory = []
computerAEntirePoints = []
computerBEntirePoints = []
iterationWinnerList = []


# return 1 for Rock, 2 for Paper and 3 for Scissors
def computer_play():
    return random.choice([1, 2, 3])


# return 1 for a tie, 2 for computer B and 3 for computer A
def game_logic(computerATurn, computerBTurn):
    global computerAPoints, computerBPoints
    if computerATurn == computerBTurn:                  # if both the party choose same value
        return 1
    elif (computerATurn % 3) < (computerBTurn % 3):     # using MOD operator to determine computer B as the winner
        computerBPoints += 1
        return 2
    else:                                               # when computer A wins
        computerAPoints += 1
        return 3


# append winner to the winnerHistory list
def append_winner_history(winner):
    global winnerHistory
    if winner == 1:
        winnerHistory.append("Tie")
    elif winner == 2:
        winnerHistory.append("Computer A")
    else:
        winnerHistory.append("Computer B")


# determine iteration winner
def iteration_winner():
    if computerAPoints == computerBPoints:
        return 1
    elif computerAPoints > computerBPoints:
        return 2
    else:
        return 3



def play_one_round():
    global historyTable
    computerATurn = computer_play()
    computerBTurn = computer_play()

    # update history list for user and computer
    computerAHistory.append(rpsList[computerATurn - 1])
    computerBHistory.append(rpsList[computerBTurn - 1])

    winner = game_logic(computerATurn, computerBTurn)
    append_winner_history(winner)


print("Welcome to the simulation of Rock, Paper and Scissors!!!")

print("Please enter the total no. of rounds you want to simulate: ", end="")
totalRoundsToSimulate = int(input())
print("Please enter the total no. of iterations you want to simulate of ", totalRoundsToSimulate, " rounds each: ", end="", sep="")
totalIterations = int(input())


allResults = []


totalRoundsToSimulateCounter = totalRoundsToSimulate
# initialize user and computer points
# computerAPoints = 0
# computerBPoints = 0

# history list
computerAHistory = []
computerBHistory = []


while totalIterations > 0:
    totalRoundsToSimulate = totalRoundsToSimulateCounter
    while totalRoundsToSimulate > 0:
        play_one_round()
        # Update total round counter
        totalRoundsToSimulate -= 1

    computerAEntireHistory.append(computerAHistory)
    computerBEntireHistory.append(computerBHistory)
    winnerEntireHistory.append(winnerHistory)
    computerAEntirePoints.append(computerAPoints)
    computerBEntirePoints.append(computerBPoints)
    iterationWinnerList.append(winnerList[iteration_winner() - 1])

    totalIterations -= 1


while True:
    print('Press:\n1. View one whole iteration\n2. View All iterations\n0.Exit')
    choice = int(input())

    if choice == 0:
        break
    elif choice == 1:
        print("Enter the iteration you want to view from 1 to ", totalIterations)
        it = int(input())

        historyTable = PrettyTable(["Round No.", "Computer A selected", "Computer B selected", "Winner"])
        print("Iteration ", it, " of the simulation was as follows and the winner of this simulation was ", iterationWinnerList[it-1])
        # add rows to the game history table
        for i in range(0, totalRoundsToSimulateCounter):
            historyTable.add_row([i + 1, computerAEntireHistory[it-1][i], computerBEntireHistory[it-1][i], winnerEntireHistory[it-1][i]])
        print(historyTable)



