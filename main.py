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

user_input = ""
first_player = True

while user_input != "exit":
    user_input = input("Enter a position from 1 to 9 (or type 'exit' to quit): ")
    if user_input.isdigit() and 1 <= int(user_input) <= 9:
        index = int(user_input) - 1
        row = index // 3
        col = index % 3
    
    if board[row][col] == "":
        if first_player:
            board[row][col] = "X"
            if check_winner("X"):
                print_board()
                print(" X wins!")
                break
            first_player = False
        else:
            board[row][col] = "O"
            if check_winner("O"):
                print_board()
                print(" O wins!")
                break
            first_player = True
    else:
        print("Cell is already taken")

   
   
        
   

    print(board)


    









