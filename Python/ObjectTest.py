class student:
    def __init__(self,name,ID,age,mark,fav):
        self.ID = ID
        self.age = age
        self.mark = mark
        self.fav = fav
        self.name = name

    def Display(self):
        print()
        print("Name:",self.name, end=",")
        print(" ID:",self.ID, end=",")
        print(" Age:",self.age, end=",")
        print(" Mark:",self.mark, end=",")
        print(" Favorite Class:",self.fav)
        print()

s1 = student("John",3423842,15,"82%","Math")
s2 = student("Bob",8639476,13,"99%","English")
s3 = student("Jimmy",2085728,17,"56%","History")

s1.Display()

