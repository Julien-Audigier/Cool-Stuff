def play(): 
    def ChooseOptions(List):
        print()
        for i in range(1,len(List)+1):
            print("{}:".format(i),List[i-1])
        print()
        Answer = input("Which game do you want to play? ")
        if Answer.isdigit():
            Answer = int(Answer)
            if Answer >= 1 and Answer <= len(List):
                return(Answer)
        print()
        print(" ~ Invalid Input ~ ")
        return(0)

    Answer = 0
    Games = ["Connect Four", "Tic-Tac-Toe", "Connect-What?","Wordle"]

    while Answer == 0:
        Answer = ChooseOptions(Games)
    
    if Answer == 1:
        import ConnectFour
    elif Answer == 2:
        import TicTacToe
    elif Answer == 3:
        import ConnectWhat
    elif Answer == 4:
        import Wordle

    for i in range(0,4):
        print()
    play()

play()