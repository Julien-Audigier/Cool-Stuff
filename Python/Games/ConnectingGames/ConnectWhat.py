import random
def Play(Player, gameboard, Conn, Grav):
        print()
        print("Player",str(Player))
        print()
        ShowBoard(gameboard)
        if Grav == "YES":
            Row = len(gameboard)-1
        else:
            Row = input("Which row? ")
        Column = input("Which column? ")

        if Column == "Kill":
            return(True)
        else:
            if Collision(Player, Column,Row, gameboard, Grav) == False:
                print("~ Invalid Input ~")
                Play(Player, gameboard, Conn, Grav)
            print()
            print("Player",str(Player))
            print()
            print("Which column?")
            CW = CheckWin(gameboard, Conn, Player)
            if CW == "Tie":
                print("Tie")
                return(True)
            elif  CW == True:
                print("Player", Player, "has won!")
                return(True)
            else:
                return(False)

def Collision(Player, Column, Row, board, Grav):
    if str(Column).isdigit() and str(Row).isdigit():
        l = int(Column)-1
        r = int(Row)-1
        if (l >= 0 and l <= len(board)) and (r >= 0 and r <= len(board)):
            if Grav == "YES":
                for i in reversed(range(len(board))):
                    if board[0][l] != 0:
                        return(False)
                    elif board[i][l] == 0:
                        board[i][l] = Player
                        return(True)
                    else:
                        continue
            else:
                if gameboard[r][l] == 0:
                    gameboard[r][l] = Player
                    return(True)
                return(False)
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

def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
    return(lstring)

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

def CheckWin(board, Conn, Player):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            try:
                points = 0
                for c in range(0, Conn):
                    if board[i+c][j] == Player: #Check Up/Down
                        points+=1
                    else:
                        break
                if points == Conn:
                    return(True)
            except IndexError:
                points = 0
            try:
                points = 0
                for c in range(0, Conn):
                    if board[i][j+c] == Player: #Check Right/Left
                        points+=1
                    else:
                        points = 0
                        break
                if points == Conn:
                    return(True)
            except IndexError:
                points = 0
            try: #Check Diagonal Left
                points = 0
                for c in range(0, Conn):
                    if board[i+c][j+c] == Player:
                        points+=1
                    else:
                        points = 0
                        break
                if points == Conn:
                    return(True)
            except IndexError:
                points = 0
            try: #Check Diagonal Right
                points = 0
                for c in range(0, Conn):
                    if board[i-c][j+c] == Player:
                        points+=1
                    else:
                        points = 0
                        break
                if points == Conn:
                    return(True)
            except IndexError:
                points = 0
                continue
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] == 0:
                return(False)
    return("Tie")

    return(''.join(lstring))

# ~ ~ ~ Main ~ ~ ~ #

Grav = 0
Conn = 0
gameboard=[]
AmPl = 0
Row = 0
Player = 1
Turns = 0
Column = 0
kill = False

while gameboard == []:
    print()
    rowtemp = []
    gameboard = []
    length = input("Enter length: ")
    if length.isdigit():
        if int(length) <= 99 and int(length) >= 3:
            for i in range(0,int(length)):
                rowtemp = []
                for i in range(0,int(length)):
                    rowtemp.append(0)
                gameboard.append(rowtemp)
            break
    print("~ Invalid Input ~")

while Conn == 0:
    print()
    Conn = input("Connect What? ")
    if str(Conn).isdigit():
        if int(Conn) >= 3 and int(Conn) <= len(gameboard):
            Conn = int(Conn)
            break
    Conn = 0
    print("~ Invalid Input ~")

while Grav == 0:
    print()
    Grav = input("Gravity? (Yes or No) ")
    Grav = Grav.upper()
    if Grav == "YES" or "NO":
            break
    Grav = 0
    print("~ Invalid Input ~")

while AmPl == 0:
    print()
    AmPl = input("How many players? ")
    if str(AmPl).isdigit():
        if int(AmPl) >= 1 and int(AmPl) <= 9:
            AmPl = int(AmPl)
            break
    AmPl = 0
    print("~ Invalid Input ~")

print()
if Grav == "YES":
    print("Welcome to Connect", Conn)
else:
    if Conn == 3:
        print("Welcome to Tic-Tac-Toe")
    else:
        print("Welcome to", end=" ")
        for i in range(0,Conn-1):
            r = random.randint(1,3)
            if r == 1:
                print("Tic",end="-")
            elif r == 2:
                print("Tac",end="-")
            else:
                print("Toe",end="-")
        print("Toe")

while (kill != True):
    Player = (Turns % AmPl) + 1
    Turns += 1
    kill = Play(Player, gameboard, Conn, Grav)