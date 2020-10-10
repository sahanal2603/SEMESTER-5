"""1BM18CS089
SAHANA L
"""

#TIC-TAC-TOE in Python

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' '+board[1] + ' | '+board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4] + ' | '+board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[7] + ' | '+board[8] + ' | ' + board[9])
    print('   |   |')
    print('')

def isWinner(bo, le):
    return (
    bo[7] == le and bo[8] == le and bo[9] == le or
    bo[4] == le and bo[5] == le and bo[6] == le or
    bo[1] == le and bo[2] == le and bo[3] == le or
    bo[1] == le and bo[4] == le and bo[7] == le or
    bo[2] == le and bo[5] == le and bo[8] == le or
    bo[3] == le and bo[6] == le and bo[9] == le or
    bo[1] == le and bo[5] == le and bo[9] == le or
    bo[3] == le and bo[5] == le and bo[7] == le 
    )

def playerMove():
    run = True
    while run:
        move = input('PLEASE SELECT A POSITION TO PLACE "X",(1 TO 9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('SORRY, THIS POSITION IS OCCUPIED!')
            else:
                print('PLEASE CHOOSE A VALID POSITION (1 TO 9)!')

        except:
            print('PLEASE SELECT A POSITION!')

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and  x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else: 
        return True

def main():
    print('PLAY TIC-TAC-TOE! \n')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner (board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('SORRY YOU LOST!! \nO\'S WON THIS TIME!')
            break

        if not(isWinner (board, 'X')):
            move = computerMove()
            if move == 0:
                print('TIE GAME!')
            else:
                insertLetter('O', move)
                print('COMPUTER PLACED AN "O" IN POSITION', move, ':')
                printBoard(board)            
        else:
            print('HURRAY YOU WON!!\nX\'S WON THIS TIME!')
            break

    if isBoardFull(board):
        print('TIE GAME!  BOARD FULL!')

main()

while True:
    answer=input('DO YOU WANT TO PLAY AGAIN (Y/N)?')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('*********************************')
        main()
    else:
        break
   
