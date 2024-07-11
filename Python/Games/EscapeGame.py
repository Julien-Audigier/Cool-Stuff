def ShowLevel(Level):
    for i in range(0,len(Level)):
        for j in range(0,len(Level[i])-1):
            print(Level[i][j], end=" ")
        print(Level[i][len(Level)-1])

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
    if Level[locY + cy][locX + cx] != "#" and Level[locY + cy][locX + cx] != "|" and Level[locY + cy][locX + cx] != "-":
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
    PlayMake()

def ChooseOptions(List,Input):
        print()
        for i in range(1,len(List)+1):
            print("{}:".format(i),List[i-1])
        print()
        Answer = input(Input)
        print()
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

def WordBank():
    WordBank = []
    f = open("Levels.txt", "r")
    for x in f:
        WordBank.append(x)
    for i in range(0,len(WordBank)):
        try:
            WBL = StringToList(WordBank[i])
            WBL.remove(WBL[len(WBL)-1])
            WordBank[i] = ''.join(WBL)
            if WordBank.count(WordBank[i]) > 1:
                WordBank.remove(WordBank[i])
        except IndexError:
            continue
    return WordBank

def PlayMake():
    Answer = 0
    Games = ["Play", "Make a Level"]

    while Answer == 0:
        Answer = ChooseOptions(Games, "What do you want to do? ")
    if Answer == 1:

        Levels = WordBank()
        Answer = 0
        while Answer == 0:
            Answer = ChooseOptions(Levels, "Which game do you want to play? ")
        filepath = "".join([Levels[Answer-1],".txt"])
        file = []
        Level = []
        with open(filepath,'r') as fileReader:
            file.append(fileReader.readlines())
        file = file[0]
        for i in range(0,len(file)-1):
                WBL = StringToList(file[i])
                WBL.remove(WBL[len(WBL)-1])
                file[i] = ''.join(WBL)
        PPS = [pressureplate(locX=1,locY=1) for _ in range(0,int(file[0]))]
        temp = 1
        for i in range(0,int(file[0])):
            PPS[i].locX = int(file[temp])
            PPS[i].locY = int(file[temp+1])
            temp+=2
        doors = [door(locX=1,locY=1,PP=PPS[0]) for _ in range(0,int(file[temp]))]
        temp += 1
        for i in range(0,int(file[temp-1])):
            doors[i].locX = int(file[temp])
            doors[i].locY = int(file[temp+1])
            doors[i].PP = PPS[int(file[temp+2])]
            temp+=3
        temp+=1
        for i in range(0,int(file[temp-1])):
            temp += 1
            RowT = []
            for i in range(0,int(file[temp-1])):
                if file[temp] == "-":
                    file[temp] = " "
                RowT.append(file[temp])
                temp+=1
            Level.append(RowT)
        LevelS = [Level,int(file[temp]),int(file[temp+1]),doors]
        Play(LevelS)
    else:
        Level = MakeLevel()
        PLocX = 1
        PLocY = 1
        Stop = False
        PPN = 0
        PPI = []
        DN = 0
        DI = []
        while Stop == False:
            ShowInv(Level)
            try:
                Row = int(input("Which row? "))
                Col = int(input("Which column? "))
                if (Row <= len(Level)-1 and Row > 0) and (Col <= len(Level)-1 and Col > 0):
                    Answer = 0
                    Games = ["Place Wall","Place Box","Place Pressureplate","Place Door","Place Player","Place End","Delete","Stop"]
                    while Answer == 0:
                        Answer = ChooseOptions(Games, "What do you want to do? ")
                    if Answer == 1:
                        temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                        Level = temp[0]
                        DI = temp[1]
                        DN = temp[2]
                        PPI = temp[3]
                        PPN = temp[4]
                        Level[Row][Col] = "#"
                    elif Answer == 2:
                        temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                        Level = temp[0]
                        DI = temp[1]
                        DN = temp[2]
                        PPI = temp[3]
                        PPN = temp[4]
                        Level[Row][Col] = "B"
                    elif Answer == 3:
                        Name = input("Enter ID of pressureplate: ")
                        if Name.isalpha():
                            temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                            Level = temp[0]
                            DI = temp[1]
                            DN = temp[2]
                            PPI = temp[3]
                            PPN = temp[4]
                            Level[Row][Col] = "*"
                            PPI.append(Name)
                            PPI.append(PPN)
                            PPI.append(Col)
                            PPI.append(Row)
                            PPN += 1
                        else:
                            print(" ~ Invalid ID ~ ")
                            continue
                    elif Answer == 4:
                        ID = input("Enter pressureplate: ")
                        if PPI.count(ID) > 0:
                            temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                            Level = temp[0]
                            DI = temp[1]
                            DN = temp[2]
                            PPI = temp[3]
                            PPN = temp[4]
                            DI.append(Col)
                            DI.append(Row)
                            DI.append(PPI[PPI.index(ID)+1])
                            Level[Row][Col] = "|"
                            DN += 1
                        else:
                            print(" ~ Invalid ID ~ ")
                            continue
                    elif Answer == 5:
                        temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                        Level = temp[0]
                        DI = temp[1]
                        DN = temp[2]
                        PPI = temp[3]
                        PPN = temp[4]
                        for i in range(0,len(Level)):
                            for j in range(0,len(Level)):
                                if Level[i][j] == "&":
                                    Level[i][j] = "-"
                                    break
                        Level[Row][Col] = "&"
                        PLocX = Col
                        PLocY = Row
                    elif Answer == 6:
                        temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                        Level = temp[0]
                        DI = temp[1]
                        DN = temp[2]
                        PPI = temp[3]
                        PPN = temp[4]
                        Level[Row][Col] = "E"
                    elif Answer == 7:
                        temp = CheckReplace(Level,DI,DN,PPI,PPN,Row,Col)
                        Level = temp[0]
                        DI = temp[1]
                        DN = temp[2]
                        PPI = temp[3]
                        PPN = temp[4]
                        Level[Row][Col] = "-"
                    elif Answer == 8:
                        Stop = True
                        Options = ["Yes","No"]
                        Answer = 0
                        while Answer == 0:
                            Answer = ChooseOptions(Options,"Do you want to save? ")
                        if Answer == 1:
                            temp = 0
                            for i in range(0,PPN):
                                PPI.remove(PPI[temp])
                                PPI.remove(PPI[temp])
                                temp += 2
                            PPI.insert(0,PPN)
                            file = PPI
                            file.append(DN)
                            for i in DI:
                                file.append(i)
                            file.append(len(Level))
                            for i in range(0,len(Level)):
                                file.append(len(Level[i]))
                                for j in Level[i]:
                                    file.append(j)
                            file.append(PLocX)
                            file.append(PLocY)
                            Name = [input("Name of Level: "),".txt"]
                            try:
                                f = open("".join(Name), "x")
                                f.close
                                f = open("Levels.txt", "a")
                                f.write(Name[0])
                                f.write("\n")
                                f.close
                                f = open("".join(Name), "x")
                            except FileExistsError:
                                if Name[0] != "Level":
                                    f = open("".join(Name), "w")
                                else:
                                    print(" ~ Cannot overide game file ~ ")
                                    continue
                            for i in file:
                                f.write(str(i))
                                f.write("\n")
                            f.close()
                            break
                        else:
                            break
            except ValueError:
                continue
        PlayMake()

def CheckReplace(Level,DI,DN,PPI,PPN,Row,Col):
    if Level[Row][Col ] == "*":
        PPN -= 1
        temp = 2
        pr = 'a'
        for o in range(0,PPN+1):
            if PPI[temp] == Col and PPI[temp+1] == Row:
                PPI.pop(temp)
                PPI.pop(temp)
                pr = PPI[temp-1]
                PPI.pop(temp-1)
                PPI.pop(temp-2)
                temp = 2
                try:
                    for k in range(0,DN):
                        if DI[temp] == pr:
                            DI.pop(temp)
                            Level[DI[temp-2]][DI[temp-1]] = "-"
                            DI.pop(temp-1)
                            DI.pop(temp-2)
                            DN -= 1
                        elif DI[temp] > o:
                            DI[temp]-=1
                            temp += 3
                        else:
                            temp += 3
                except IndexError:
                    temp = 2
                    pass
                temp = 2
            else:
                if str(pr).isdigit():
                    if pr < PPI[temp-1]:
                        PPI[temp-1] -= 1
                temp += 4
    elif Level[Row][Col ] == "|":
        temp = 2
        for k in range(0,DN):
            if DI[temp] == Col and DI[temp+1] == Row:
                DI.pop(temp)
                DI.pop(temp-1)
                DI.pop(temp-2)
                DN =- 1
            else:
                temp += 1
    return(Level,DI,DN,PPI,PPN)

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
            if ((Level[self.locY+1][self.locX] == "E" or Level[self.locY-1][self.locX] == "E") or (Level[self.locY+1][self.locX] == "|" or Level[self.locY-1][self.locX] == "|")) or (Level[self.locY][self.locX+1] == "#" and Level[self.locY][self.locX-1] == "#"):
                Level[self.locY][self.locX] = "-"
            else:
                Level[self.locY][self.locX] = "|"
            return(Level)

PlayMake()