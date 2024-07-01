Thing = [1,2,3,4,5,6,7,8]
print(Thing)
for i in range(len(Thing)-1,-1, -1):
    Temp = Thing[i]
    Thing.remove(Temp)
    Thing.append(Temp)
print(Thing)

