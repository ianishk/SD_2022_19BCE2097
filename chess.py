print("------------welocome to chess game------------")
print("press e to exit the game")
board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]

def printBoard():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

p1Chars = input("player 1 input: ")
p1CharList = p1Chars.split()
for i in p1CharList:
    i = "A-"+i
board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], p1CharList]
printBoard()
p2Chars = input("player 2 input: ")
p2CharList = p1Chars.split()
for i in p2CharList:
    i = "A-"+i
board = [p2CharList, ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], p1CharList]

while True:    
    p1Move = input("player 1 move: ")
    if p1Move == "e":
        break
    
    print(p1CharList)

