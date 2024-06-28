import math
Points = 0
print()
if input("What is 1 + 1? ") == "2":
    Points += 1
if input("Is 1 = 2? ") == "No" or "no":
    Points += 1
if input("What are the first 18 digits of pi? ") == "3.14159265358979323":
    Points += 1
if input("What is my first name? ") == "Julien" or "julien":
    Points += 1
if input("What is my last name? ") == "Audigier":
    Points += 1
print("you got", Points * 20,"percent.")
print()