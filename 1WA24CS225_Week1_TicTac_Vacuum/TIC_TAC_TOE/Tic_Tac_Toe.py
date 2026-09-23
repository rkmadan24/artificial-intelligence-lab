# Tic-Tac-Toe Game

board = [" " for _ in range(9)]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(symbol):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == symbol and
            board[position[1]] == symbol and
            board[position[2]] == symbol):
            return True

    return False

def board_full():
    return " " not in board


# Game starts
while True:
    display_board()

    # Human move
    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = "X"

    if check_winner("X"):
        display_board()
        print("Human Wins!")
        break

    if board_full():
        display_board()
        print("Draw!")
        break

    # Computer move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

    if check_winner("O"):
        display_board()
        print("Computer Wins!")
        break

    if board_full():
        display_board()
        print("Draw!")
        break
