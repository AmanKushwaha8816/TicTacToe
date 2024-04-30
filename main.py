from random import randrange


def display_board(board):
    print(f'''+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')

    x = False

    if (len(make_list_of_free_fields(board)) == 0):
        x = victory_for(board, "X")
        x = victory_for(board, "O")

        if x == False:
            print("Game Done its a Draw")

    elif (turn == 0):
        if (0 < len(make_list_of_free_fields(board)) <= 4):
            x = victory_for(board, "O")

        if x == False:
            draw_move(board)


    else:
        if (0 < len(make_list_of_free_fields(board)) <= 4):
            x = victory_for(board, "X")

        if x == False:
            enter_move(board)


def enter_move(board):
    try:
        x = int(input("Enter Your Move: "))

        if (1 <= x <= 9):
            if (x < 4):
                a, b = 0, x - 1

            elif (x < 7):
                a, b = 1, x - 4

            else:
                a, b = 2, x - 7

            board = [list(x) for x in board]

            if (x in make_list_of_free_fields(board)):
                board[a][b] = "O"

            else:
                raise ValueError

            global turn
            turn = 0
            board = [tuple(x) for x in board]
            display_board(board)

        else:
            raise ValueError


    except:
        print("something went wrong please check you input")
        enter_move(board)


def make_list_of_free_fields(board):
    global avail_Spaces
    avail_Spaces = []
    for nested in board:
        avail_Spaces += [x for x in nested if (x != "X" and x != "O")]

    return avail_Spaces


def victory_for(board, sign):
    win = False
    winner = sign

    if (board[0][0] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[2][0] == "X"):
        win = True

    else:
        for a in range(0, 3):
            vertical = []
            horizontal = []
            for b in range(0, 3):
                vertical.append(board[b][a])

                horizontal.append(board[a][b])

            if (all(x == sign for x in vertical) or all(v == sign for v in horizontal)):
                win = True

    if (sign == "X" and win):
        print("CPU won!")
        return True
    elif (sign == "O" and win):
        print("You won!")
        return True
    else:
        return False


def draw_move(board):
    board = [list(x) for x in board]

    x = randrange(8)
    if x < 3:
        i = 0
        j = x

    elif x < 6:
        i = 1
        j = x - 3

    else:
        i = 2
        j = x - 6

    if (board[i][j] != "X" and board[i][j] != "O"):
        board[i][j] = "X"

        global turn
        turn = 1
        board = [tuple(x) for x in board]
        display_board(board)

    else:
        draw_move(board)


turn = 1

list1 = [(1, 2, 3), (4, "X", 6), (7, 8, 9)]

display_board(list1)
