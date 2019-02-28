# Battleship

# Instance Variables

displayBoard = [[" ", "1", "2", "3", "4", "5"],["a", "o", "o", "o", "o", "o"],["b", "o", "o", "o", "o", "o"],["c", "o", "o", "o", "o", "o"],["d", "o", "o", "o", "o", "o"],["e", "o", "o", "o", "o", "o"]]
realBoard1 = [["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"]]
realBoard2 = [["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"]]
playBoard1 = [["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"]]
playBoard2 = [["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"],["o", "o", "o", "o", "o"]]



# Print Game Board #


print("Welcome to the world's best battleship game!")
print("")
print("")
print("This is your game board.")
print()
print()


# Set Battleship Locations #

# Methods

a = 0
alp = ""
num = 0

def defineAlp(alp):
    if(alp == 'a'):
        a = 0
        return a
    if(alp == 'b'):
        a = 1
        return a
    if(alp == 'c'):
        a = 2
        return a
    if(alp == 'd'): 
        a = 3
        return a
    else:
        a = 4
        return a


def chooseLoc1(alp, num):
    realBoard1[alp][num] = "x"
    return realBoard1


def chooseLoc2(alp, num):
    realBoard2[alp][num] = "x"
    return realBoard2

def chooseTrap1(alp, num, board):
    board[alp][num] = "@"
    return board

def chooseTrap2(alp, num, board):
    board[alp][num] = "@"
    return board


def guessLoc1(alp, num):
    if(realBoard2[alp][num] == "x" ):
        playBoard2[alp][num] = "*"
    else:
        playBoard2[alp][num] = "-"
    for r in playBoard2:
        for c in r:
            print(c, end = " ")
        print()


def guessLoc2(alp, num):
    if(realBoard1[alp][num] == "x"):
        playBoard1[alp][num] = "*"
    else:
        playBoard1[alp][num] = "-"
    for r in playBoard1:
        for c in r:
            print(c, end = " ")
        print()


def printBoard(board):
    for r in board:
        for c in r:
            print(c, end = " ")
        print()

    
def checkGameEnds(board):
    count = 0
    for r in board:
        for c in r:
            if(c == "*"):
                count += 1
    if(count == 5):
        return "true"
    else:
        return "false"

        
# Set Ships #
# Player 1

printBoard(displayBoard)

count1 = 1
while True:
    if(count1 == 6):
        break
    
    print("")
    print("")
    alp1 = input("Choose the location of your %dst battleship (alphabet)" %count1)
    num1 = int(input("Choose the location of your %dst battleship (number)" %count1))
    count1 += 1

    newBoard1 = chooseLoc1(defineAlp(alp1), num1 - 1)
    printBoard(newBoard1)
    
alpT = input("Choose the location of the trap (alphabet)")
numT = int(input("Choose the location of the trap (number)"))
chooseTrap1(defineAlp(alpT), numT - 1, realBoard1)
printBoard(realBoard1) 


# Player 2

for n in range(50):
    print("")

printBoard(displayBoard)
    
count2 = 1
while True:
    if(count2 == 6):
        break
    
    print("")
    print("")
    alp2 = input("Choose the location of your %dst battleship (alphabet)" %count2)
    num2 = int(input("Choose the location of your %dst battleship (number)" %count2))
    count2 += 1

    newBoard2 = chooseLoc2(defineAlp(alp2), num2 - 1)
    printBoard(newBoard2)

alpT = input("Choose the location of the trap (alphabet)")
numT = int(input("Choose the location of the trap (number)"))
chooseTrap2(defineAlp(alpT), numT - 1, realBoard2)
printBoard(realBoard2)


# Play! #

for n in range(50):
    print("")
    
print("Both players finished setting their ships. Let's start the game.")

print("First, player 1 starts the game. Try to crash the batteship")

move = 1
move1 = 1
move2 = 1
canMove1 = True
canMove2 = True

while True:
    
        
    if(move % 3 != 0):
        
        for n in range(5):
           print("")

        print("Player 1")   
        print("Move %d" %move1)
        printBoard(playBoard2)
        guess1 = input("Choose the location of your guess (alphabet)")
        guess2 = int(input("Choose the location of guess (number)"))

        guessLoc1(defineAlp(guess1), guess2 - 1)
        if (checkGameEnds(playBoard2) == "true"):
            print("------------------------------------------------------------")
            print("Player 1 wins! You've become the heir Jack Sparrow!")
            print("------------------------------------------------------------")
            break
        elif (realBoard2[defineAlp(guess1)][guess2 - 1] == "@"):
            print("--------------------------------------------------------------------------")
            print("You got caught in a trap! You cannot participate in one turn from now on.")
            print("--------------------------------------------------------------------------")
            canMove1 = False

        move1 += 1   
        if(canMove1 == False and canMove2 == True):
            move += 2
        elif(canMove1 == True and canMove2 == False):
            move += 3
            canMove2 = True
        else:
            move += 1


            
                 
    elif(move % 3 == 0):

        for n in range(5):
           print("")

        print("Player 2")
        print("Move %d" %move2)
        printBoard(playBoard1)
        guess1 = input("Choose the location of your guess (alphabet)")
        guess2 = int(input("Choose the location of guess (number)"))

        guessLoc2(defineAlp(guess1), guess2 - 1)
        if (checkGameEnds(playBoard1) == "true"):
            print("------------------------------------------------------------")
            print("Player 2 wins! You've become the heir Jack Sparrow!")
            print("------------------------------------------------------------")
            break
        elif (realBoard1[defineAlp(guess1)][guess2 - 1] == "@"):
            print("--------------------------------------------------------------------------")
            print("You got caught in a trap! You cannot participate in one turn from now on.")
            print("--------------------------------------------------------------------------")
            canMove2 = False
            
        move2 += 1
        if(canMove1 == False and canMove2 == True):
            move += 3
            canMove1 = True
        elif(canMove1 == True and canMove2 == False):
            move += 2
        else:
            move += 2

        

            

        
   









