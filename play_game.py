#tic tac toe game
import random
board=[[1,2,3],[4,5,6],[7,8,9]]
def print_board(board):
    print(("-"*7).join("++++"))
    print((" "*7).join("||||"))
    print("|" + "   " + "{}".format(board[0][0]) + "   " + "|"  + "   " + "{}".format(board[0][1]) + "   " + "|"+\
         "   " + "{}".format(board[0][2]) + "   " + "|" )
    print((" " * 7).join("||||"))
    print(("-" * 7).join("++++"))
    print((" " * 7).join("||||"))
    print("|" + "   " + "{}".format(board[1][0]) + "   " + "|" + "   " + "{}".format(board[1][1]) + "   " + "|" + \
          "   " + "{}".format(board[1][2]) + "   " + "|")
    print((" " * 7).join("||||"))
    print(("-" * 7).join("++++"))
    print((" " * 7).join("||||"))
    print("|" + "   " + "{}".format(board[2][0]) + "   " + "|" + "   " + "{}".format(board[2][1]) + "   " + "|" + \
          "   " + "{}".format(board[2][2]) + "   " + "|")
    print((" " * 7).join("||||"))
    print(("-" * 7).join("++++"))


def winner():
    # user check
    user="O"
    comp="X"
    other="You are tied"
    if board[0][0]==board[0][1]==board[0][2]=="O":
        return user
    elif board[1][0]==board[1][1]==board[1][2]=="O":
        return user
    elif board[2][0]==board[2][1]==board[2][2]=="O":
        return user
    elif board[0][0]==board[1][1]==board[2][2]=="O":
        return user
    elif board[0][2]==board[1][1]==board[2][0]=="O":
        return user
    elif board[0][0]==board[1][0]==board[2][0]=="O":
        return user
    elif board[0][2]==board[1][2]==board[2][2]=="O":
        return user
    elif board[0][1]==board[1][1]==board[2][1]=="O":
        return user
    #computer check
    elif board[0][0]==board[0][1]==board[0][2]=="X":
        return comp
    elif board[1][0]==board[1][1]==board[1][2]=="X":
        return comp
    elif board[2][0]==board[2][1]==board[2][2]=="X":
        return comp
    elif board[0][0]==board[1][1]==board[2][2]=="X":
        return comp
    elif board[0][2]==board[1][1]==board[2][0]=="X":
        return comp
    elif board[0][0]==board[1][0]==board[2][0]=="X":
        return comp
    elif board[0][2]==board[1][2]==board[2][2]=="X":
        return comp
    elif board[0][1]==board[1][1]==board[2][1]=="X":
        return comp
    elif all(num not in [item for sublist in board for item in sublist] for num in range(1,10)):
        return other
    return False

def computer_turn():
    print("it\'s computers turn:")
    while True:
        comp = random.randint(1,9)
        comp=comp-1
        row = comp // 3
        col = comp % 3
        if board[row][col] in [1,2,3,4,5,6,7,8,9]:
            board[row][col]="X"
            print_board(board)
            break

def user():
    print("it\'s your turn:")
    while True:
        try:
            move=int(input("select a number from 1 to 9:"))-1
            row=move//3
            col=move%3
            if board[row][col] in [1,2,3,4,5,6,7,8,9]:
                board[row][col]="O"
                print_board(board)
                break
            print("invalid number, try again")
        except:
            print("you entered a wrong number or charecter, please selecta number from number 1 to 9:")

def play_game():
    print(" welcom to a tic tac toe")
    print_board(board)
    while True:
        computer_turn()
        x=winner()
        if x :
            if x=="X":
                print("computer is winner")
            elif x=="You are tied":
                print("You are tied")
            break
        user()
        x=winner()
        if x:
            if x=="O":
                print(" you are winner")
            elif x=="You are tied":
                print("You are tied")
            break
play_game()
