from posixpath import split


print("------------welocome to chess game------------")
print("press e to exit the game")

board = [["-   " for i in range(5)] for j in range(5)]

def printBoard():
    print()
    for p in board:
        for q in p:
            print(q, end=" ")
        print()
    print()

p1Chars = input("player 1 input: ")
p1CharList = p1Chars.split()
for i in range(0, 5):
    board[4][i] = "A-"+p1CharList[i]

printBoard()
p2Chars = input("player 2 input: ")
p2CharList = p1Chars.split()
for i in range(0, 5):
    board[0][i] = "B-"+p2CharList[i]

printBoard()
while True: 
    flag = True   
    p1Move = input("player 1 move: ")
    if p1Move == "e":
        print("thank you")
        break
    p1MoveDetail = p1Move.split(":")
    for i in range(0, 5):
        if flag == False:
            break
        for j in range(0, 5):
            if(board[i][j] == "A-"+p1MoveDetail[0]):
                if(p1MoveDetail[1] == "F"):
                    if i-1 >= 0 and board[i-1][j].split("-")[0] != "A":
                        board[i][j] = "-   "
                        board[i-1][j] = "A-"+p1MoveDetail[0]
                        printBoard()
                    else:
                        print("invalid input")
                    flag = False
                    break
                elif(p1MoveDetail[1] == "L"):
                    if j-1 >= 0 and board[i][j-1].split("-")[0] != "A":
                        board[i][j] = "-   "
                        board[i][j-1] = "A-"+p1MoveDetail[0]
                        printBoard()
                    else:
                        print("Invalid input")
                    flag = False
                    break
                elif(p1MoveDetail[1] == "R"):
                    if j+1 < 5 and board[i][j+1].split("-")[0] != "A":
                        board[i][j] = "-   "
                        board[i][j+1] = "A-"+p1MoveDetail[0]
                        printBoard()
                    else:
                        print("Invalid input")
                    flag = False
                    break
                elif(p1MoveDetail[1] == "B"):
                    if i+1 < 5 and board[i+1][j].split("-")[0] != "A":
                        board[i][j] = "-   "
                        board[i+1][j] = "A-"+p1MoveDetail[0]
                        printBoard()
                    else:
                        print("Invalid input")
                    flag = False
                    break
                else:
                    print("Invalid input")
                break
    
    flag = True
    p2Move = input("player 2 move: ")
    if p2Move == "e":
        print("thank you")
        break
    p2MoveDetail = p2Move.split(":")
    for i in range(0, 5):
        if flag == False:
            break
        for j in range(0, 5):
            if(board[i][j] == "B-"+p2MoveDetail[0]):
                if(p2MoveDetail[1] == "F"):
                    if i+1 < 5 and board[i+1][j].split("-")[0] != "B":
                        board[i][j] = "-   "
                        board[i+1][j] = "B-"+p2MoveDetail[0]
                        printBoard()
                        
                    else:
                        print("Invalid input")
                    flag = False
                    break
                    
                elif(p2MoveDetail[1] == "L"):
                    if j+1 < 5 and board[i][j+1].split("-")[0] != "B":
                        board[i][j] = "-   "
                        board[i][j+1] = "B-"+p2MoveDetail[0]
                        printBoard()
                        flag = False
                    else:
                        print("Invalid input")
                    break
                    
                elif(p2MoveDetail[1] == "R"):
                    if j-1 >= 0 and board[i][j-1].split("-")[0] != "B":
                        board[i][j] = "-   "
                        board[i][j-1] = "B-"+p2MoveDetail[0]
                        printBoard()
                        
                    else:
                        print("Invalid input")
                    flag = False
                    break
                elif(p2MoveDetail[1] == "B"):
                    if i-1 >= 0 and board[i-1][j].split("-")[0] != "B":
                        board[i][j] = "-   "
                        board[i-1][j] = "B-"+p2MoveDetail[0]
                        printBoard()
                        
                    else:
                        print("invalid input")
                    flag = False
                    break
                else:
                    print("Invalid input")
                break
