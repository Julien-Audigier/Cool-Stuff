def ShowN(Length):
    print("  ", end="  ") 
    for i in range(1,Length+1):
        temp = str(i)
        if temp[len(temp)-1] == '0':
            temp = temp[0]
        else:
            temp = temp[len(temp)-1]
        if i < Length:
            print(temp, end="   ")
            continue
        print(temp)


PlayerBoard = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
Aph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

ShowN(len(PlayerBoard)-1)

print(" ",end=" ")
for j in range(0,len(PlayerBoard[0])):
    print("+",end="")
    print("-",end="")
    print("-",end="")
    print("-",end="")
print("+")
for i in range(0,len(PlayerBoard)-1):
    print(Aph[i],end="")
    print(" | ",end="")
    for j in range(0,len(PlayerBoard[i])):
        print(PlayerBoard[i][j],end=" | ")
    print(Aph[i % 26])
    print(" ",end=" ")
    for j in range(0,len(PlayerBoard[i])):
        print("+",end="")
        print("-",end="")
        print("-",end="")
        print("-",end="")
    print("+")

ShowN(len(PlayerBoard)-1)