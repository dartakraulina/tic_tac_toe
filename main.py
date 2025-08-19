import tkinter as tk
import numpy as np

# -------------------- GAME-LOGIC -----------------------------


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

def restart():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player[0] = "X"
    canvas.delete("all")

    for i in range(1, 3):
        canvas.create_line(i * 100, 0, i * 100, 300)
        canvas.create_line(0, i * 100, 300, i * 100)

    turn_label.config(text="X turn")
    outcome_label.config(text="")

    canvas.bind("<Button-1>", clicking)
    print("Game restarted!")

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
    print(row,col)
    print(f"this is {current_player}'s turn")

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


    if check_winner(board, current_player[0]):
        outcome_label.config(text=f"{current_player[0]} wins!")
        turn_label.config(text="")
        canvas.unbind("<Button-1>")
        return
    
    if is_draw(board):
        outcome_label.config(text="Draw!")
        turn_label.config(text="")
        canvas.unbind("<Button-1>")
        return

    current_player[0] = "O" if current_player[0] == "X" else "X"
    turn_label.config(text=f"{current_player[0]} turn")

  




restart_button = tk.Button(window, text="Restart", font=("Arial", 12), command=restart)
restart_button.pack(pady=10)



canvas.bind("<Button-1>", clicking)



window.mainloop()



