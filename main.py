import numpy as np

board = np.full((3, 3), "", dtype=str)

def print_board():
    for row in board:
        print(row)

def check_winner(sym):
    for i in range(3):
        if all(cell == sym for cell in board[i]):
            return True
    for i in range(3):
        if all(board[j][i] == sym for j in range(3)):
            return True
    if all(board[i][i] == sym for i in range(3)):
        return True
    if all(board[i][2-i]== sym for i in range(3)):
        return True
    return False

def is_draw():
    return all(cell != "" for row in board for cell in row)

def make_move(row, col, sym):
    board[row][col] = sym

user_input = ""
first_player = True

while True:
    user_input = input("Enter a position from 1 to 9 (or type 'exit' to quit): ")

    if user_input == "exit":
        break
    if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
        print("Invalid input.")
        continue

    index = int(user_input) - 1
    row = index // 3
    col = index % 3

    if board[row][col] != "":
        print("Cell is already taken")
        continue

    sym = "X" if first_player else "O"
    make_move(row, col, sym)
    print_board()  

    if check_winner(sym):
        print(f"{sym} wins!")
        break

    if is_draw():
        print("It's a draw!")
        break

    first_player = not first_player
