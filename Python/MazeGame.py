import random

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
                    rowtemp.append("#")
                gameboard.append(rowtemp)
            break
    print("~ Invalid Input ~")

Col = 0
Row = random.randint(2,)