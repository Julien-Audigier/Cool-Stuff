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
    if Level[locY + cy][locX + cx] != "#" and Level[locY + cy][locX + cx] != "|":
        if Level[locY + cy][locX + cx] == "B" and Level[locY + (2 * cy)][locX + (2 * cx)] != "#" and Level[locY + (2 * cy)][locX + (2 * cx)] != "B":
            Level[locY + (2 * cy)][locX + (2 * cx)] = "B"
            return([Level,True])
        elif Level[locY + cy][locX + cx] != "B":
            return([Level,True])
    return([Level,False])

def checkPD(P,D,Level):
    temp = P.checkShow(Level)
    Level = temp[0]
    D.checkOpen(Level,temp[1])

class pressureplate:
    def __init__(self,locX, locY):
        self.locX = locX
        self.locY = locY

    def checkShow(self,Level):
        if Level[self.locY][self.locX] == " " or Level[self.locY][self.locX] == "*":
            Level[self.locY][self.locX] = "*"
            return([Level, False])
        else:
            return([Level, True])
p1 = pressureplate(2,5)
p2 = pressureplate(1,5)

class door:
    def __init__(self,locX, locY):
        self.locX = locX
        self.locY = locY

    def checkOpen(self,Level,open):
        if open == True:
            if Level[self.locY][self.locX] == "&":
                Level[self.locY][self.locX] = "&"
            else:
                Level[self.locY][self.locX] = " "
            return(Level)
        else:
            Level[self.locY][self.locX] = "|"
            return(Level)
d1 = door(5,6)
d2 = door(4,6)


Level = [
    ["#","#","#","#","#","#","#","#"],
    ["#","&"," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#","B","B","#","#","#","#","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#"," "," "," ","#","#","#","#"],
    ["#"," "," "," "," "," ","E","#"],
    ["#","#","#","#","#","#","#","#"]]

locX = 1
locY = 1

while Level != True:
    checkPD(p1,d1,Level)
    checkPD(p2,d2,Level)
    ShowLevel(Level)
    temp = Move(Level,locX,locY)
    Level = temp[0]
    locX = temp[1]
    locY = temp[2]
print("You Won")