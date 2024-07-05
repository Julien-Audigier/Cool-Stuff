import random

def StringToList(string):
    lstring = []
    for i in range(0, len(str(string))):
        string = str(string)
        lstring.append(string[i])
    return(lstring)

def ShowBoard(Board):
    for i in range(0,len(Board)):
        for j in range(0,(len(Board[0])-1)):
            print(Board[i][j],end=" ")
        print(Board[i][(len(Board[0])-1)])

def PrintList(List):
    if List == []:
        print()
        print("There are no unavailable letters.")
        return
    print(", ".join(List))

def WordBank():
    WordBank = []
    f = open("sgb-words.txt", "r")
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

WordBank5 = WordBank()

Board = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]

Row = 0
Guess = 0

Word = (str(WordBank5[random.randint(0,len(WordBank5))])).lower()
LetterBank = StringToList(Word)
unavailableletters = []

while Guess != Word:
    Guess = 0
    ShowBoard(Board)
    while Guess == 0:
        print()
        Guess = input("Guess word or enter 1 to check unavailable letters: ")
        
        try:
            if int(Guess) == 1:
                PrintList(unavailableletters)
        except ValueError:
            if Guess.isalpha():
                Guess = Guess.lower()                       #Checking Quess
                LGuess = StringToList(Guess)
                if WordBank5.count(Guess) > 0:
                    if len(LGuess) == len(LetterBank):
                        break
            print()
            print("Not a word")
        Guess = 0

    for i in range(0,len(LGuess)):
        if LetterBank.count(LGuess[i]) == 0:
            unavailableletters.append(LGuess[i])
            LGuess[i] = "#"
        if LetterBank[i] == LGuess[i]:
            LGuess[i] = str(LGuess[i]).upper()
        Board[Row][i] = LGuess[i]
    print(unavailableletters)
    if Row == len(Board):
        break
    Row += 1
print()
print("The word was",Word)