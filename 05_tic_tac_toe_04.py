#check conditions of input
'''
to allow two players
player 1=X
player 2=O
'''
"""
00 01 02
10 11 12
20 21 22 
"""
board=[["_","_","_"],["_","_","_"],["_","_","_"]]
numberOfMoves=9
def printBoard(board):
    for row in board:
        for column in row:
            print(column,end="   ")
        print("\n")

def takeInput(player):
    user_input=input(f"(PLAYER {player})Enter any position from 1 to 9 or enter q to quit: ")
    if checkValidInput(user_input,board)==False:
        print("check positions and enter again!!!")
        user_input=takeInput(player)
    return user_input

def checkValidInput(user_input,board):
    user_input=int(user_input)
    user_input=int(user_input)-1
    row=int(user_input/3)
    column=int(user_input%3)
    if(user_input>=0 and user_input<10 and board[row][column]=="_"):
        return True
    else:
        return False

#printBoard(board)
def fillPositions(user_input,board,value):
    user_input=int(user_input)-1
    row=int(user_input/3)
    column=int(user_input%3)
    board[row][column]=value

def exitGame(user_input):
    if user_input=='q':
        return True
    else:
        return False

def checkWinner(board,value):
    #checking rows,columns and diagonols
    if(board[0][0]==board[1][0]==board[2][0]==value or board[0][1]==board[1][1]==board[2][1]==value or board[0][2]==board[1][2]==board[2][2]==value):
        return True
    elif(board[0][0]==board[0][1]==board[0][2]==value or board[1][0]==board[1][1]==board[1][2]==value or board[2][0]==board[2][1]==board[2][2]==value):
        return True
    elif(board[0][0]==board[1][1]==board[2][2]==value or board[0][2]==board[1][1]==board[2][0]==value):
        return True
    else:
        return False

while True:
    #player 1
    
    user1_input=takeInput("1")
    numberOfMoves=numberOfMoves-1
    if exitGame(user1_input)==True:
        print("Thanks for playing!")
        break
    else:
        fillPositions(user1_input,board,"X")
    print("PLAYER 1 = X    PLAYER 2 = O")
    printBoard(board)
    if checkWinner(board,"X")==True:
        print("Yaay PLAYER 1 won.")
        break
    
    #player 2
    
    user2_input=takeInput("2")
    numberOfMoves=numberOfMoves-1
    if exitGame(user2_input)==True:
        print("Thanks for playing!")
        break
    else:
        fillPositions(user2_input,board,"O")
    print("PLAYER 1 = X    PLAYER 2 = O")
    printBoard(board)

    if checkWinner(board,"O")==True:
        print("Yaay PLAYER 2 won.")
        break



