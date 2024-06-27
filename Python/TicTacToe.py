import math
def ShowBoard(Board):
    print()
    print(" ", end=" ")
    for i in range(1, len(Board[0])+1):
        if  getlastdigit(i) != 0:
            Temp = getlastdigit(i)
        else:
            Temp = getfirstdigit(i)
        if i == len(Board):
            print(Temp)
        else:
            print(Temp, end=" ")
    for x in range(0,len(Board)):
        print(x+1,end=" ")
        for y in range(0,len(Board[x])):
            print(Board[x][y], end =" ")
        print(x+1)
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
            for n in range(1,len(str(digit))):
                num1 *= 10
            digit -= num1
    return digit

GameBoard = [["_","_","_"],["_","_","_"],["_","_","_"]]
ShowBoard(GameBoard)