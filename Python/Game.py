def ShowLevel(Level):
    for i in range(0,8):
        for j in range(0,7):
            print(Level[i][j], end=" ")
        print(Level[i][7])

def Move(Level,locX,locY,turns):
    Where = input("w, a, s, or d: ").lower()
    Level[locY][locX] = " "
    if Where == "w":
        temp = collison(Level, locX, 0, locY, -1)
        if temp[1] == True:
            Level = temp[0]
            locY -= 1
            turns += 1
    if Where == "s":
        temp = collison(Level, locX, 0, locY, 1)
        if temp[1] == True:
            Level = temp[0]            
            locY += 1
            turns += 1
    if Where == "a":
        temp = collison(Level, locX, -1, locY, 0)
        if temp[1] == True:
            Level = temp[0]           
            locX -= 1
            turns += 1
    if Where == "d":
        temp = collison(Level, locX, 1, locY, 0)
        if temp[1] == True:
            Level = temp[0]               
            locX += 1
            turns += 1
    if Where == "kill" or Level[locY][locX] == "E":
        Level[locY][locX] = "&"
        ShowLevel(Level)
        return(True,locX,locY,turns)
    Level[locY][locX] = "&"
    return([Level,locX,locY,turns])

def collison(Level,locX,cx,locY,cy):
    if Level[locY + cy][locX + cx] != "#" and Level[locY + cy][locX + cx] != "|":
        if Level[locY + cy][locX + cx] == "B" and Level[locY + (2 * cy)][locX + (2 * cx)] != "#" and Level[locY + (2 * cy)][locX + (2 * cx)] != "B":
            Level[locY + (2 * cy)][locX + (2 * cx)] = "B"
            return([Level,True])
        elif Level[locY + cy][locX + cx] != "B":
            return([Level,True])
    return([Level,False])

def Play(LevelS):
    Level = LevelS[0]
    locX = LevelS[1]
    locY = LevelS[2]
    doors = LevelS[3]
    turns = 0
    while Level != True:
        for i in doors:
            i.checkOpen(Level)
        ShowLevel(Level)
        temp = Move(Level,locX,locY,turns)
        Level = temp[0]
        locX = temp[1]
        locY = temp[2]
        turns = temp[3]
    print("You Won in",turns,"turns!")

def ChooseOptions(List):
        print()
        for i in range(1,len(List)+1):
            print("{}:".format(i),List[i-1])
        print()
        Answer = input("What do you want to do: ")
        if Answer.isdigit():
            Answer = int(Answer)
            if Answer >= 1 and Answer <= len(List):
                return(Answer)
        print()
        print(" ~ Invalid Input ~ ")
        return(0)

def MakeLevel():
    Length = 0
    Level = []

    while Level == []:
        print()
        rowtemp = []
        Level = []
        Length = input("Enter Length: ")
        if Length.isdigit():
            Length = int(Length) + 2
            if Length <= 50 and Length >= 6:
                for i in range(0,Length):
                    rowtemp = []
                    for i in range(0,Length):
                        rowtemp.append("-")
                    Level.append(rowtemp)
                break
        print("~ Invalid Input ~")

    for i in range(0,len(Level)):
        for j in range(0,len(Level)):
            if i == 0 or j == 0 or i == len(Level)-1 or j == len(Level)-1:
                Level[i][j] = "#"
    return(Level)

def ShowInv(Level):

    ShowN(len(Level)) #Top Number

    for i in range(0,len(Level)):
        if i > 0 and i < len(Level)-1:
            ltemp = StringToList(i)
            temp = ltemp[len(ltemp)-1]
        else:
            temp = " "
        print(temp,end=" ")
        for j in range(0,len(Level)):
            print(Level[i][j], end=" ") #Level
        
        print(temp) #Right Numbers
    
    ShowN(len(Level)) #Bottom Numbers

def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
    return(lstring)

def ShowN(Length):
    print("   ", end=" ") 
    for i in range(1,Length-2):
        ltemp = StringToList(i)
        temp = ltemp[len(ltemp)-1]
        if temp == "0":
            print(ltemp[0], end=" ")
        else:
            print(temp, end=" ")
    print(Length-2)

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

class door:
    def __init__(self,locX, locY, PP):
        self.locX = locX
        self.locY = locY
        self.PP = PP

    def checkOpen(self,Level):
        temp = self.PP.checkShow(Level)
        Level = temp[0]
        if temp[1] == True:
            if Level[self.locY][self.locX] == "&":
                Level[self.locY][self.locX] = "&"
            else:
                Level[self.locY][self.locX] = " "
            return(Level)
        else:
            Level[self.locY][self.locX] = "|"
            return(Level)

Answer = 0
Games = ["Play", "Make a Level"]

while Answer == 0:
    Answer = ChooseOptions(Games)
if Answer == 1:
    Level = [
    ["#","#","#","#","#","#","#","#"],
    ["#","&"," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#","B","B","#","#","#","#","#"],
    ["#"," "," "," "," "," "," ","#"],
    ["#"," "," "," ","#","#","#","#"],
    ["#"," "," "," "," "," ","E","#"],
    ["#","#","#","#","#","#","#","#"]]
    PPS = [pressureplate(locX=1,locY=1) for _ in range(0,2)]
    PPS[0].locX = 1
    PPS[0].locY = 5
    PPS[1].locX = 2                                             #Level 1
    PPS[1].locY = 5
    doors = [door(locX=1,locY=1,PP=PPS[0]) for _ in range(0,2)]
    doors[0].locX = 5
    doors[0].locY = 6
    doors[0].PP = PPS[0]
    doors[1].locX = 4
    doors[1].locY = 6
    doors[1].PP = PPS[1]
    LevelS = [Level,1,1,doors]
    Play(LevelS)
else:
    Level = MakeLevel()
    Stop = False
    while Stop == False:
        ShowInv(Level)
        try:
            Row = int(input("Which row? "))
            Col = int(input("Which column? "))
            if (Row <= len(Level) and Row > 0) and (Col <= len(Level) and Col > 0):
                Answer = 0
                Games = ["Place Wall","Place Pressureplate","Place Door","Place Player","Place End","Delete","Stop"]
                while Answer == 0:
                    Answer = ChooseOptions(Games)
                if Answer == 1:
                    Level[Row][Col] = "#"
                elif Answer == 2:
                    pass
                elif Answer == 3:
                    pass
                elif Answer == 4:
                    for i in range(0,len(Level)):
                        for j in range(0,len(Level)):
                            if Level[i][j] == "&":
                                Level[i][j] = "-"
                                break
                    Level[Row][Col] = "&"
                    PLocX = Col
                    PLocY = Row
                elif Answer == 5:
                    Level[Row][Col] = "E"
                elif Answer == 6:
                    Level[Row][Col] = "-"
                elif Answer == 7:
                    Stop = True
        except ValueError:
            continue
