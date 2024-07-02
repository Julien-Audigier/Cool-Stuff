def Play(Player):
        print()
        print("Player",str(Player))
        print()
        ShowBoard()
        Column = input("Which column? ")
        if Column == "Kill":
            return(True)
        else:
            if Collision(Player, Column) == False:
                Play(Player)
            print()
            print("Player",str(Player))
            print()
            ShowBoard()
            print("Which column?")
            CW = CheckWin()
            if CW == "Tie":
                print("Tie")
                return(True)
            elif  CW == True:
                print("Player", Player, "has won!")
                if input("continue? "):
                    return(True)
            return(False)

def Collision(Player, Column):
    if str(Column).isdigit():
        Column = int(Column)
        if  (Column > 0 and Column < 8):
            Row = 5
            Column -= 1
            while gameboard[Row][Column] != 0 and Row != 0:
                Row -= 1
            if Row == 0 and gameboard[Row][Column] != 0:
                return(False)
            else:
                gameboard[Row][Column] = Player
                return(True)
    return(False)
        
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
        for j in range(0,7):
            try:
                if gameboard[i][j] == gameboard[i+1][j] == gameboard[i+2][j] == gameboard[i+3][j] != 0: #Check Up/Down
                    return(True)
            except IndexError:
                continue
            try:
                if gameboard[i][j] == gameboard[i][j+1] == gameboard[i][j+2] == gameboard[i][j+3] != 0: #Check Right/Left
                    return(True)
            except IndexError:
                continue
            try: #Check Diagonal
                if (gameboard[i][j] == gameboard[i+1][j+1] == gameboard[i+2][j+2] == gameboard[i+3][j+3] != 0) or (gameboard[i][j] == gameboard[i+1][j-1] == gameboard[i+2][j-2] == gameboard[i+3][j-3] != 0):
                    return(True)
            except IndexError:
                continue
    for i in range(0,6):
        for j in range(0,7):
            if gameboard[i][j] == 0:
                return(False)
    return("Tie")

# ~ ~ ~ Vars ~ ~ ~ #

gameboard=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

Row = 0
Player = 1
Turns = 0
Column = 0
win = False
kill = False

# ~ ~ ~ Main ~ ~ ~ #

while (kill != True):
    Player = (Turns % 2) + 1
    Turns += 1
    kill = Play(Player)
    # Repeat1