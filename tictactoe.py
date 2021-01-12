def printboard(board):
    print(board[0])
    print(board[1])
    print(board[2])

def check_win(board):
    if(board[0][0]==board[0][1] and board[0][0]==board[0][2]):
                                     return(1)
    elif(board[0][0]==board[1][0] and board[0][0]==board[2][0]):
                                     return(1)
    elif(board[0][0]==board[1][1] and board[0][0]==board[2][2]):
                                     return(1)
    elif(board[0][2]==board[1][2] and board[0][2]==board[2][2]):
                                     return(1)
    elif(board[2][0]==board[2][1] and board[2][0]==board[2][2]):
                                     return(1)
    elif(board[0][1]==board[1][1] and board[0][1]==board[2][1]):
                                     return(1)
    elif(board[1][0]==board[1][1] and board[1][0]==board[1][2]):
                                     return(1)
    elif(board[0][1]==board[1][1] and board[0][0]==board[2][0]):
                                     return(1)



    
                 
name_x=input("Please enter player name for x :")
name_o=input("Please enter player name for o :")

board=[[[],[],[]],[[],[],[]],[[],[],[]]]

printboard(board)

for i in range(9):
    if(i%2==0):
        print("It is "+name_x+"'s turn")
        row=int(input("Enter row number to play your turn :"))
        col=int(input("Enter column number to play your turn :"))
        board[row][col].append('x')
        print("Your turn has been played!")
        printboard(board)
        if(check_win(board)==1):
           print("Yayy! "+name_x+" won!")
           break;
    else:
        print("It is "+name_o+"'s turn")
        row=int(input("Enter row number to play your turn :"))
        col=int(input("Enter column number to play your turn :"))
        board[row][col].append('o')
        print("Your turn has been played!")
        printboard(board)
        if(check_win(board)==1):
           print("Yayy! "+name_o+" won!")
           break;

        
