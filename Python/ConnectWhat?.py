def Play(Player, gameboard):
        print()
        print("Player",str(Player))
        print()
        ShowBoard(gameboard)
        Column = input("Which column? ")
        if Column == "Kill":
            return(True)
        else:
            if Collision(Player, Column) == False:
                Play(Player, gameboard)
            print()
            print("Player",str(Player))
            print()
            ShowBoard(gameboard)
            print("Which column?")
            CW = CheckWin()
            if CW == "Kill":
                print("Tie")
                return(True)
            elif  CW == True:
                print("Player", Player, "has won!")
                return(True)
            else:
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
        
def ShowBoard(Board):

    ShowN(len(Board)) #Top Number

    for i in range(0,len(Board)):
        ltemp = StringToList(i+1)
        temp = ltemp[len(ltemp)-1]
        if temp == "0":
            print(ltemp[0], end=" ") #Left Numbers
        else:
            print(temp, end=" ")
        
        for j in range(0,len(Board)):
            print(Board[i][j], end=" ") #Board
        
        print(temp) #Right Numbers
    
    ShowN(len(Board)) #Bottom Numbers


def ShowN(Length):
    print(" ", end=" ") 
    for i in range(1,Length):
        ltemp = StringToList(i)
        temp = ltemp[len(ltemp)-1]
        if temp == "0":
            print(ltemp[0], end=" ")
        else:
            print(temp, end=" ")
    print(Length)

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

def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
    return(lstring)
    return(''.join(lstring))

# ~ ~ ~ Vars ~ ~ ~ #

gameboard=[]

Row = 0
Player = 1
Turns = 0
Column = 0
win = False
kill = False

# ~ ~ ~ Main ~ ~ ~ #

while gameboard == []:
    Row = []
    gameboard = []
    length = input("Enter length: ")
    if length.isdigit():
        if int(length) <= 30:
            while len(Row) != int(length):
                Row.append("0")
            while len(gameboard) != int(length):
                gameboard.append(Row)
while (kill != True):
    Player = (Turns % 2) + 1
    Turns += 1
    kill = Play(Player, gameboard)
    # Repeat1