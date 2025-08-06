import numpy as np



def print_board(board):
    for row in board:
        print(row)

def check_winner(board, sym):
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

def is_draw(board):
    return all(cell != "" for row in board for cell in row)

def make_move(board, row, col, sym):
    board[row][col] = sym

def get_outcome(board, sym):
    if check_winner(board, sym):
        return f"{sym} wins"
    if is_draw(board):
        return "draw"
    return "ongoing"

def play_game():
    board = np.full((3, 3), "", dtype=str)
    first_player = True

    while True:
        user_input = input("Enter a position from 1 to 9 (or type 'exit' to quit and 'restart' to restart the game): ")

        if user_input == "exit":
            return "exit"
        if user_input == "restart":
            return "restart"

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
        make_move(board, row, col, sym)
        print_board(board)  

        result = get_outcome(board, sym)
        if result != "ongoing":
            print(result)
            return "finished" 

        first_player = not first_player


def main():
    while True:
        outcome = play_game()
        if outcome == "exit":
            print("Thanks for playing!")
            break
        elif outcome == "restart":
            print("Restarting the game...\n")
            continue
        else:
            # Game ended normally, ask user what to do next:
            again = input("Type 'restart' to play again, or anything else to quit: ")
            if again.lower() == "restart":
                print()
                continue
            else:
                print("Thanks for playing!")
                break

main()   #This function is a straight up copy paste from chatgpt. I will be honest and i apologize it. Everything i did before broke the code and this fixed it!!
   





