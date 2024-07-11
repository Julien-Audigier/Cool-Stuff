
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
Games = ["Connect Four", "Tic-Tac-Toe", "Connect-What?","Wordle", "Random Number Game","Escape Game"]

while Answer == 0:
    Answer = ChooseOptions(Games)
    
if Answer == 1:
    import Games.ConnectingGames.ConnectFour as ConnectFour
elif Answer == 2:
    import Games.ConnectingGames.TicTacToe as TicTacToe
elif Answer == 3:
    import Games.ConnectingGames.ConnectWhat as ConnectWhat
elif Answer == 4:
    import Games.WordleFiles.Wordle as Wordle
elif Answer == 5:
    import Games.RandomNumberGame as RandomNumberGame
elif Answer == 6:
    import Games.EscapeGame as EscapeGame
