import math

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

def CheckWin(Player,Row,Column, Board):
    if Row == 1:
        if (Board[Row - 1][Column] == Player) and (Board[Row +1][Column] == Player):
            return(True)
        if Column == 1:
            if ((Board[Row - 1][Column-1] == Player) and (Board[Row +1][Column+1] == Player) or (Board[Row - 1][Column+1] == Player) and (Board[Row +1][Column-1] == Player)):
                return(True)
    if Row == 2:
        if (Board[Row - 1][Column] == Player) and (Board[Row -2][Column] == Player):
            return(True)
        if Column == 2:
            if (Board[Row - 1][Column-1] == Player) and (Board[Row -2][Column-2] == Player):
                return(True)
        if Column == 0:
            if (Board[Row - 1][Column+1] == Player) and (Board[Row -2][Column+2] == Player):
                return(True)
    if Row == 0:
        if (Board[Row + 1][Column] == Player) and (Board[Row +2][Column] == Player):
            return(True)
        if Column == 0:
            if (Board[Row + 1][Column+1] == Player) and (Board[Row +2][Column+2] == Player):
                return(True)
        if Column == 2:
            if (Board[Row + 1][Column-1] == Player) and (Board[Row +2][Column-2] == Player):
                return(True)
    if Column == 0:
        if (Board[Row][Column+1] == Player) and (Board[Row][Column+2] == Player):
            return(True)
    if Column == 1:
        if (Board[Row][Column+1] == Player) and (Board[Row][Column-1] == Player):
            return(True)
    if (Board[Row][Column-1] == Player) and (Board[Row][Column-2] == Player):
        return(True)
    return(False)





def Play(Player, Board, Turn):
    SwPl = False
    while SwPl == False:
        ShowBoard(Gameboard, Turn)
        print()
        Row = input("Which row? ")
        Column = input("Which Column? ")
        if  Row == "Kill" or Column == "Kill":
            print()
            return([])
        if Row.isdigit() and Column.isdigit():
            Row = int(Row)
            Column = int(Column)
            Row = round(Row)
            Column = round(Column)
            if (Row <= 3 and Row >= 1) and (Column <= 3 and Column >= 1) and (Board[Row-1][Column-1] == "_"):
                Board[Row-1][Column-1] = Player
                SwPl = True
                if CheckWin(Player, Row-1, Column-1, Board) == True:
                    ShowBoard(Gameboard, Turn)
                    print()
                    print("Player", (Turn % 2)+1,"won!")
                    print()
                    return([])
                else:
                    return(Board)
        SwPl = False

Turn = 0
Player = "x"
Gameboard = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

while Turn <= 42 or Gameboard != []:
    Gameboard = Play(Player, Gameboard, Turn)
    if Gameboard == []:
        break
    if Player == "x":
        Player = "o"
    elif Player == "o":
        Player = "x"
    Turn += 1