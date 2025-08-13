import tkinter as tk
import numpy as np

# -------------------- GAME-LOGIC -----------------------------
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
    if all(board[i][2-i] == sym for i in range(3)):
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

# -------------------- GUI -----------------------------
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(width=False, height=False)


frame = tk.Frame(window)
frame.pack()

turn_label = tk.Label(frame, text="X turn", font=("Arial", 14))
turn_label.pack(pady=5)

canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack()

for i in range(1, 3):
    canvas.create_line(i * 100, 0, i * 100, 300)
    canvas.create_line(0, i * 100, 300, i * 100)

# Load images
O_img = tk.PhotoImage(file="letter-o.png").subsample(2, 2)
X_img = tk.PhotoImage(file="close.png").subsample(3,3)


current_player = ["X"]  
board = [["" for _ in range(3)] for _ in range(3)]

outcome_label = tk.Label(window, text="", font=("Arial", 12), fg="green")
outcome_label.pack(pady=5)

def clicking(event):
    row = event.y // 100
    col = event.x // 100

    if board[row][col] != "":
        return
    
    if current_player[0] == "O":
        img = O_img
    else:
        img = X_img

    x_center = col * 100 + 50
    y_center = row * 100 + 50

    canvas.create_image(x_center, y_center, image=img)
    board[row][col] = current_player[0]

    current_player[0] = "O" if current_player[0] == "X" else "X"
    turn_label.config(text=f"{current_player[0]} turn")

    if all(cell != "" for row in board for cell in row):
        outcome_label.config(text="Game is over. You are a loser at life")
        turn_label.config(text="")


def restart_clicked():
    print("Nespied mani vēl ludzu. Es vēl nestrādāju!")

restart_button = tk.Button(window, text="Restart", font=("Arial", 12), command=restart_clicked)
restart_button.pack(pady=10)



canvas.bind("<Button-1>", clicking)



window.mainloop()



