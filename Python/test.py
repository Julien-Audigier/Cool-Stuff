import math
Hat = [4,11,51,23,67,88,11,10]
print("The sum is", sum(Hat))
print("The max is", max(Hat))
for i in range(0,len(Hat)-1):
    Num = Hat[i]
    ocr = 0
    for o in range(0,len(Hat)-1):
        if Hat[o] == Num:
            ocr += 1
            if ocr > 1:
                Hat.pop(i)
    print(Num,"occures",ocr)
print(Hat)

def getfirstdigit(num):
    num = float(num)
    while num >= 10:
       num /= 10
    num -= .9
    num = math.ceil(num)
    return int(num)

def getlastdigit(num):
    digit = num
    for i in range(1,len(str(num))):
        if len(str(digit)) != 1:
            num1 = getfirstdigit(digit)
            for n in range(0,(int(len(str(digit)))-1)):
                num1 *= 10
            digit -= num1
    return digit

print(getlastdigit(100))
print(getfirstdigit(10))