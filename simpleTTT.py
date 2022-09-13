board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
winner = '-'
onTurn = 'X'
winNum = {
    -10:'O',
     10:'X'
}

def printBoard():
    print()
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
        print()
    print()

def checkLeft():
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':
                return True
    return False

def checkWinner():
    for r in range(3):
        if board[r][0]==board[r][1] and board[r][1]==board[r][2]:
            if board[r][0]=='X':
                return 10
            elif board[r][0]=='O':
                return -10

    for c in range(3):
        if board[0][c]==board[1][c] and board[1][c]==board[2][c]:
            if board[0][c]=='X':
                return 10
            elif board[0][c]=='O':
                return -10

    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[1][1]=='X':
                return 10
        elif board[1][1]=='O':
                return -10

    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[1][1]=='X':
                return 10
        elif board[1][1]=='O':
                return -10
    
    return 0

def main():
    global winner, onTurn

    while winner=='-':
        printBoard()
        if checkWinner()!=0 or checkLeft()==0:
            break
        print(f"player {onTurn} is on turn!")

        if onTurn=='X':
            i = int(input("(x)>"))
            j = int(input("(y)>"))

            if (j>=0 and i>=0 and j<3 and i<3) and board[i][j]=='-':
                board[i][j]='X'
                onTurn='O'
            else:
                continue

        else:
            i = int(input("(x)>"))
            j = int(input("(y)>"))

            if (j>=0 and i>=0 and j<3 and i<3) and board[i][j]=='-':
                board[i][j]='O'
                onTurn='X'
            else:
                continue

    winner=checkWinner()
    if winner==10 or winner==-10:
        print(f"player {winNum[winner]} won!")
    else:
        print("tie!")

if __name__=="__main__":
    main()
