import math
x = 2
def getfirstdigit(num):
    num = float(num)
    while num > 10:
       num /= 10
    num -= .9
    num = math.ceil(num)
    return int(num)

def getlastdigit(num):
    digit = num
    for i in range(1,len(str(num))):
        if len(str(digit)) != 1:
            num1 = getfirstdigit(digit)
            for n in range(1,len(str(digit))):
                num1 *= 10
            digit -= num1
    return digit
print(x)     
print(getfirstdigit(x))
print(getlastdigit(x))