def StringToList(string):
    lstring = []
    for ObjL in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[ObjL])
    return(lstring)

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

filepath = "ObjL.txt"
ObjL = []
with open(filepath,'r') as fileReader:
    ObjL.append(fileReader.readlines())
ObjL = ObjL[0]
for i in range(0,len(ObjL)-1):
        WBL = StringToList(ObjL[i])
        WBL.remove(WBL[len(WBL)-1])
        ObjL[i] = ''.join(WBL)
PPS = [pressureplate(locX=1,locY=1) for _ in range(0,int(ObjL[0]))]
temp = 1
for i in range(0,int(ObjL[0])):
    PPS[i].locX = int(ObjL[temp])
    PPS[i].locY = int(ObjL[temp+1])
    temp+=2
    print(PPS[i].locX,PPS[i].locY)
doors = [door(locX=1,locY=1,PP=PPS[0]) for _ in range(0,int(ObjL[temp]))]
temp += 1
for i in range(0,int(ObjL[temp-1])):
    doors[i].locX = int(ObjL[temp])
    doors[i].locY = int(ObjL[temp+1])
    doors[i].PP = PPS[int(ObjL[temp+2])]
    temp+=3
    print(doors[i].locX,doors[i].locY,doors[i].PP)