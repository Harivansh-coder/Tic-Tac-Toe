"""
    Following script is two players tic tac toe game.
    Game ends when either of the player win as usual.
"""
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def show_board():
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print()


def check_win(mark):
    return (  # rows check
            board[0][0] == board[0][1] == board[0][2] == mark or
            board[1][0] == board[1][1] == board[1][2] == mark or
            board[2][0] == board[2][1] == board[2][2] == mark or
            # columns check
            board[0][0] == board[1][0] == board[2][0] == mark or
            board[0][1] == board[1][1] == board[2][1] == mark or
            board[0][2] == board[1][2] == board[2][2] == mark or
            # diagonal check
            board[0][0] == board[1][1] == board[2][2] == mark or
            board[0][2] == board[1][1] == board[2][0] == mark)


def check_tie(y):
    for i in board:
        if '-' in i and y == False:
            return
    return "Tie"



def pos_in():
    while True:
        pos = int(input("Enter position (1 - 9): "))
        if pos == 1:
            return [0, 0]
        elif pos == 2:
            return [0, 1]
        elif pos == 3:
            return [0, 2]
        elif pos == 4:
            return [1, 0]
        elif pos == 5:
            return [1, 1]
        elif pos == 6:
            return [1, 2]
        elif pos == 7:
            return [2, 0]
        elif pos == 8:
            return [2, 1]
        elif pos == 9:
            return [2, 2]


def play():
    show_board()
    y = False
    while not y:
        for mark in 'XO':
            print(f"player {mark} turn")
            pos = pos_in()
            if board[pos[0]][pos[1]] == '-':
                board[pos[0]][pos[1]] = mark
            else:
                raise Exception("Position already taken")

            y = check_win(mark)
            s = check_tie(y)
            print(y)
            show_board()
            if y:
                print(f"player {mark} is the winner")
                break
            if s == "Tie":
                print("It's a Tie")
                y = True
                break

play()


