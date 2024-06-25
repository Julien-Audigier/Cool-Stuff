def showboard():
    print()
    print("   1  2  3  4  5  6  7")
    print(1,gameboard[0])
    print(2,gameboard[1])
    print(3,gameboard[2])
    print(4,gameboard[3])
    print(5,gameboard[4])
    print(6,gameboard[5])

def Gravity(Player,Row,Column): #Check
    if gameboard[Row][Column] == 0:
        gameboard[Row][Column]=Player
        showboard()
        
    else:
        Gravity(Player,Row-1,Column)

def place(Player):
#    TA SHENANIGANS DO NOT DELETE
   Column = input("Which Column 1-7 ")
   Temp=int(Column)
   Column=Temp
   Column -= 1
#     End TA SHENANIGANS
   Gravity(Player,5,Column)

def Start(Player):
    showboard()
    for i in range(0,42):
        Player = (i%2)+1
        place(Player)
# Begin Runtime Game~ ~ ~ ~ ~ ~ ~ ~
#Before Start

gameboard=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
Column = 0
win = 0

#Start____
Start(1)