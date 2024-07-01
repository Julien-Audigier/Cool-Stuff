import math

#Functions

def ShowBoard(Board):
    print()
    print(" ", end=" ")
    for i in range(1, len(Board[0])+1): # Top Numbers
        if  getlastdigit(i) != 0:
            Temp = getlastdigit(i)
        else:
            Temp = getfirstdigit(i)
        if i < len(Board[0]):
            print(Temp, end=" ")
        else:
            print(Temp)
    for x in range(0,len(Board)):
        if  getlastdigit(x+1) != 0: # Right Numbers
            Temp = getlastdigit(x+1)
        else:
            Temp = getfirstdigit(x+1)
        print(Temp, end=" ")
        for y in range(0,len(Board[x])):
            print(Board[x][y], end =" ") #Prints Board
        if  getlastdigit(x+1) != 0: # Left Numbers
            Temp = getlastdigit(x+1)
        else:
            Temp = getfirstdigit(x+1)
        print(Temp)
    print(" ", end=" ")
    for i in range(1, len(Board[0])+1): # Bottom Numbers
        if  getlastdigit(i) != 0:
            Temp = getlastdigit(i)
        else:
            Temp = getfirstdigit(i)
        if i < len(Board[0]):
            print(Temp, end=" ")
        else:
            print(Temp)
    print()

def getfirstdigit(num):
    num = float(num)
    while num > 10:
       num /= 10
    num -= .9
    num = math.ceil(num)
    return int(num)

def getlastdigit(num):
    digit = num
    for i in range(1,len(str(num))):
        if len(str(digit)) != 1:
            num1 = getfirstdigit(digit)
            for n in range(0,(int(len(str(digit)))-1)):
                num1 *= 10
            digit -= num1
            if digit < 0:
                digit = 1
    return digit

def CreateBoard ():
    print()
    Length = input("Enter Length: ")
    Rows = []
    Columns = []
    if Length.isdigit() and int(Length) >=1 and int(Length) <= 99:
        for i in range(0,int(Length)):
            Columns.append("_")
        for i in range(0,int(Length)):
            Rows.append(Columns)
        return Rows
    elif Length == "Kill":
        Length = "Kill"
    else:
        print()
        print("~invalid input~")
        return Rows
    
def Play(Turn, AmPl, Board):
    Player = (Turn % (AmPl))+1
    SwitchPL = False
    while SwitchPL == False:
        Row = None
        Column = None
        ShowBoard(Board)
        Row = input("Player {} which row? ".format(Player))
        Column = input("Player {} which column? ".format(Player))
        if Row.isdigit() and Column.isdigit():
            Row = int(Row)
            Column = int(Column)
            if (Row > len(Board)) or (Column > len(Board)) or (Row < 1) or (Column < 1):
                SwitchPL == False
                break
            SwitchPL = True
            print(Board)
                        Board[0][0] = Player
            return Board
        elif Row or Column == "kill":
            return False
        else:
            SwitchPL == False
            break

#Vars

Conn = 0
AmPl = None
GameBoard = []
Kill = False
Player = 0
Turn = 0


#Start

while len(GameBoard) == 0:
    GameBoard = CreateBoard()

while AmPl == None:
    AmPl = input("How many players? ")
    print()
    if AmPl.isdigit():
        AmPl = int(AmPl)
        if AmPl < 0 or AmPl > 10:
            print("~invalid input~")
            AmPl = None
            print()
    else:
       print("~invalid input~")
       AmPl = None
       print()

while Conn == 0:
    Conn = input("Connect... ")
    print()
    if Conn.isdigit():
        Conn = int(Conn)
        if Conn < 1 or Conn > len(GameBoard):
            print("~invalid input~")
            Conn = 0
            print()
    else:
       print("~invalid input~")
       Conn = 0
       print()

while Kill == False and Turn != (len(GameBoard)**2):
    GameBoard = Play(Turn, AmPl, GameBoard)
    if GameBoard == False:
        Kill = True
    else:
        Kill = False
    Turn += 1