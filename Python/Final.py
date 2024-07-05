def ShowLevel(Level):
    for i in range(0,8):
        for j in range(0,7):
            print(Level[i][j], end=" ")
        print(Level[i][7])

def Move(Level,locX,locY):
    Where = input("w, a, s, or d: ").lower()
    Level[locY][locX] = " "
    if Where == "w":
        temp = collison(Level, locX, 0, locY, -1)
        if temp[1] == True:
            Level = temp[0]
            locY -= 1
    if Where == "s":
        temp = collison(Level, locX, 0, locY, 1)
        if temp[1] == True:
            Level = temp[0]            
            locY += 1
    if Where == "a":
        temp = collison(Level, locX, -1, locY, 0)
        if temp[1] == True:
            Level = temp[0]           
            locX -= 1
    if Where == "d":
        temp = collison(Level, locX, 1, locY, 0)
        if temp[1] == True:
            Level = temp[0]               
            locX += 1
    if Where == "kill" or Level[locY][locX] == "E":
        Level[locY][locX] = "&"
        ShowLevel(Level)
        return(True,locX,locY)
    Level[locY][locX] = "&"
    return([Level,locX,locY])

def collison(Level,locX,cx,locY,cy):
    if Level[locY + cy][locX + cx] != "#":
        if Level[locY + cy][locX + cx] == "B" and Level[locY + (2 * cy)][locX + (2 * cx)] == " ":
            Level[locY + (2 * cy)][locX + (2 * cx)] = "B"
            return([Level,True])
        elif Level[locY + cy][locX + cx] != "B":
            return([Level,True])
    return([Level,False])

class presserplate:
    def __init__(self,locX, locY):
        self.locX = locX
        self.locY = locY

    def checkShow(self,locX,locY,Level):
        if Level[locY,locX] == " ":
            Level[locY,locX] == "*"
        return Level
p1 = presserplate(2,5)

Level = [
    ["#","#","#","#","#","#","#","#"],
    ["#","&"," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#","#","#","B","#","#","#","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#"," "," "," "," ","#","#","#"],
    ["#"," "," "," "," ","|","E","#"],
    ["#","#","#","#","#","#","#","#"]]

locX = 1
locY = 1

while Level != True:
    ShowLevel(Level)
    temp = Move(Level,locX,locY)
    Level = temp[0]
    locX = temp[1]
    locY = temp[2]
print("You Won")