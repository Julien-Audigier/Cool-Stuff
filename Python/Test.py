
def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
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

filepath = "PPS.txt"
PPI = []
with open(filepath,'r') as fileReader:
    PPI.append(fileReader.readlines())
PPI = PPI[0]
for i in range(0,len(PPI)-1):
        WBL = StringToList(PPI[i])
        WBL.remove(WBL[len(WBL)-1])
        PPI[i] = ''.join(WBL)
PPI[0]
print(PPI)
PPS = [door(locX=1,locY=1) for _ in range(0,2)]

filepath = "doors.txt"
doorI = []
with open(filepath,'r') as fileReader:
    doorI.append(fileReader.readlines())
doorI = doorI[0]
for i in range(0,len(doorI)-1):
        WBL = StringToList(doorI[i])
        WBL.remove(WBL[len(WBL)-1])
        doorI[i] = ''.join(WBL)
doorI[0]
print(doorI)
doors = [door(locX=1,locY=1,PP=PPS[0]) for _ in range(0,doorI[0])]

