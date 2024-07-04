def ShowBoard(Board, Turn):
    print()
    print()
    print("Player {}'s turn:".format((Turn % 2)+1))
    print()
    print("  1 2 3")
    for x in range(0,3):
        print(x+1,end=" ")
        for y in range(0,3):
            print(Board[x][y], end=" ")
        print(x +1)
    print("  1 2 3")

def CheckWin(Board):
    for i in range(0,3):
            if Board[i][0] == Board[i][1] == Board[i][2] != "_": #Check Right/Left
                return(True)
    for u in range(0,3):
            if Board[0][u] == Board[1][u] == Board[2][u] != "_": #Check Up/Down
                return(True)
    if (Board[0][0] == Board[1][1] == Board[2][2] != "_") or (Board[0][2] == Board[1][1] == Board[2][0] != "_"): #Check Diagonal
        return(True)
    return(False)

def Play(Player, Board, Turn):
    SwPl = False
    while SwPl == False:
        ShowBoard(Gameboard, Turn)
        print()
        Row = input("Which row? ")
        Column = input("Which Column? ")
        if Row.isdigit() and Column.isdigit():
            Row = int(Row)
            Column = int(Column)
            Row = round(Row)
            Column = round(Column)
            if (Row <= 3 and Row >= 1) and (Column <= 3 and Column >= 1) and (Board[Row-1][Column-1] == "_"):
                Board[Row-1][Column-1] = Player
                SwPl = True
                if CheckWin(Board) == True:
                    ShowBoard(Gameboard, Turn)
                    print()
                    print("Player", (Turn % 2)+1,"won!")
                    print()
                    return([])
                else:
                    return(Board)
        elif  Row.upper == "Kill" or Column.upper == "Kill":
            print()
            return([])
        SwPl = False

Turn = 0
Player = "x"
Gameboard = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

while Turn <= 9 or Gameboard != []: