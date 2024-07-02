
def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
    return(lstring)


def ListToString(lstring):
    return(''.join(lstring))


print()
x = StringToList(str(input("string = ")))
print(x)
x = ListToString(x)
print(x)
print()