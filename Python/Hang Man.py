import math

def comaMake(num):
    lnum = []
    digit = num
    for i in range(1,len(str(num))):
        if len(str(digit)) != 1:
            num1 = getfirstdigit(digit)
            lnum.append(num1)
            for n in range(0,(int(len(str(digit)))-1)):
                num1 *= 10
            digit -= num1
            if digit < 0:
                digit = 1
    return lnum

def getfirstdigit(num):
    num = float(num)
    while num > 10:
       num /= 10
    num = math.floor(num)
    return int(num)

print(getfirstdigit(0))

x = int(input("Factoral of: "))
for i in range(x-1,0,-1):
    x *= i
x = comaMake(x)
print(x)