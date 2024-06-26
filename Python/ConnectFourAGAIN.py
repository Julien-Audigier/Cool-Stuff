import math
def Play(Player):
    print()
    print("Player",str(Player))
    print()
    ShowBoard()
    Column = input("Which column? ")
    if Column == "Kill":
        return True
    else:
        Collision(Player, Column)

        

def Collision(Player, Column):

    if Column.isdigit():
        Column = int(Column)
        if  Column > 0 and Column < 8:
            Row = 5
            Column -= 1
            while gameboard[Row][Column] != 0:
                Row -= 1
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




# ~ ~ ~ MAIN ~ ~ ~ #
gameboard=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

Row = 0
Player = 1
Turns = 0
Column = 0
win = False
autokill = False

while (autokill != True and win != True and Turns < 41):
    Player = (Turns % 2) + 1
    Turns += 1
    autokill = Play(Player)
    # Winchek (Eventually)
    # Repeat
