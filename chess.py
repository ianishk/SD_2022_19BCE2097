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
        break
    p1MoveDetail = p1Move.split(":")
    for i in range(0, 5):
        if flag == False:
            break
        for j in range(0, 5):
            if(board[i][j] == "A-"+p1MoveDetail[0]):
                if(p1MoveDetail[1] == "F"):
                    board[i][j] = "-   "
                    board[i-1][j] = "A-"+p1MoveDetail[0]
                    printBoard()
                    flag = False
                    break
                elif(p1MoveDetail[1] == "L"):
                    board[i][j] = "-   "
                    board[i][j-1] = "A-"+p1MoveDetail[0]
                    printBoard()
                    flag = False
                    break
                elif(p1MoveDetail[1] == "R"):
                    board[i][j] = "-   "
                    board[i][j+1] = "A-"+p1MoveDetail[0]
                    printBoard()
                    flag = False
                    break
                elif(p1MoveDetail[1] == "B"):
                    printBoard()
                else:
                    board[i][j] = "-   "
                    board[i+1][j] = "A-"+p1MoveDetail[0]
                    printBoard()
                    flag = False
                    break
                break
    
    p2Move = input("player 2 move: ")
    if p2Move == "e":
        break
