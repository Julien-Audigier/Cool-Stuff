import math
def Play(Player, PSwitch):
    while PSwitch == False:
        print()
        print("Player",str(Player))
        print()
        ShowBoard()
        Column = input("Which column? ")
        if Column == "Kill":
            return True
        else:
            PSwitch = Collision(Player, Column)
            print()
            print("Player",str(Player))
            print()
            ShowBoard()
            print("Which column?")
            if CheckWin() == True:
                return True
            else:
                return False

def Collision(Player, Column):
    if Column.isdigit():
        Column = int(Column)
        if  (Column > 0 and Column < 8):
            Row = 5
            Column -= 1
            while gameboard[Row][Column] != 0 and Row != 0:
                Row -= 1
            if Row == 0 and gameboard[Row][Column] != 0:
                return False
            else:
                gameboard[Row][Column] = Player
                return True
        else:
            return False
    else:
        return False
        
def ShowBoard():
    print(" 1  2  3  4  5  6  7")
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])
    print(gameboard[3])
    print(gameboard[4])
    print(gameboard[5])

def CheckWin():
    for i in range(0,6):
        for o in range(0,4):
            if gameboard[i][o] == gameboard[i][o+1] == gameboard[i][o+2] == gameboard[i][o+3] != 0:
                return(True)
        for a in range(6,1,-1):
            if gameboard[i][a] == gameboard[i][a-1] == gameboard[i][a-2] == gameboard[i][a-3] != 0:
                return(True)
    for u in range(0,7):
        for g in range(0,3):
            if gameboard[g][u] == gameboard[g+1][u] == gameboard[g+2][u] == gameboard[g+3][u] != 0:
                return(True)
        for k in range(5,1,-1):
            if gameboard[k][u] == gameboard[k-1][u] == gameboard[k-2][u] == gameboard[k-3][u] != 0:
                return(True)
    


# ~ ~ ~ Vars ~ ~ ~ #
gameboard=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

PSwitch = False
Row = 0
Player = 1
Turns = 0
Column = 0
win = False
kill = False

# ~ ~ ~ Main ~ ~ ~ #

while (kill != True and Turns < 41):
    Player = (Turns % 2) + 1
    Turns += 1
    kill = Play(Player, PSwitch)
    # Repeat
