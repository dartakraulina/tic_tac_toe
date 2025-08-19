import tkinter as tk
import numpy as np

# -------------------- GAME-LOGIC -----------------------------


def check_winner(board, sym):
    for i in range(3):
        if all(cell == sym for cell in board[i]):
            return [(i,j) for j in range(3)]
    for i in range(3):
        if all(board[j][i] == sym for j in range(3)):
           return [(j, i) for j in range(3)]
    if all(board[i][i] == sym for i in range(3)):
        return [(i, i) for i in range(3)]
    if all(board[i][2-i] == sym for i in range(3)):
        return [(i, 2 - i) for i in range(3)]
    return None

def check_draw(board):
    return all(cell != "" for row in board for cell in row)

def restart():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player[0] = "X"
    canvas.delete("all")


    canvas.create_image(0,0, image=bg_img)
    for i in range(1, 3):
        canvas.create_line(i * 100, 0, i * 100, 300, fill='white')
        canvas.create_line(0, i * 100, 300, i * 100, fill='white')

    turn_label.config(text="X turn")
    outcome_label.config(text="")

    canvas.bind("<Button-1>", clicking)
    

# -------------------- GUI -----------------------------
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(width=False, height=False)
window.configure(bg="#DEC69C")


frame = tk.Frame(window,bg="#DEC69C" )
frame.pack()

turn_label = tk.Label(frame, text="X turn", font=("Arial", 14), bg="#DEC69C", fg='white')
turn_label.pack(pady=5)

canvas = tk.Canvas(window, width=300, height=300, bg="white")
canvas.pack(padx=50, pady=10)

bg_img = tk.PhotoImage(file="gradient-cactus.png").subsample(1,1)

canvas.create_image(0,0, image=bg_img)

for i in range(1, 3):
    canvas.create_line(i * 100, 0, i * 100, 300, fill='white')
    canvas.create_line(0, i * 100, 300, i * 100, fill='white')


current_player = ["X"]  
board = [["" for _ in range(3)] for _ in range(3)]

outcome_label = tk.Label(window, text="", font=("Arial", 12), fg="#8ca064", bg="#DEC69C")
outcome_label.pack(pady=5)

def clicking(event):
    row = event.y // 100
    col = event.x // 100

    if board[row][col] != "":
        return
    
    x_center = col * 100 + 50
    y_center = row * 100 + 50
    color = '#b2657b' if current_player[0] == "X" else "#8ca064" 

    canvas.create_text(x_center, y_center,text=current_player[0], font=("Arial", 36, "bold"), fill=color)
    board[row][col] = current_player[0]

    winning_cells = check_winner(board, current_player[0])
    if winning_cells:
        outcome_color = '#b2657b' if current_player[0] == "X" else "#8ca064"
        outcome_label.config(text=f"{current_player[0]} wins!", fg=outcome_color)
        turn_label.config(text="")

        x1 = winning_cells[0][1] * 100 + 50
        y1 = winning_cells[0][0] * 100 + 50
        x2 = winning_cells[-1][1] * 100 + 50
        y2 = winning_cells[-1][0] * 100 + 50
        canvas.create_line(x1, y1, x2, y2, width=5, fill=outcome_color)

        canvas.unbind("<Button-1>")
        return
    
    if check_draw(board):
        outcome_label.config(text="Draw!", fg="gray")
        turn_label.config(text="")
        canvas.unbind("<Button-1>")
        return


    current_player[0] = "O" if current_player[0] == "X" else "X"
    turn_label.config(
        text=f"{current_player[0]} turn",
        fg='#b2657b' if current_player[0] == "X" else "#8ca064"
    )


restart_button = tk.Button( window, text="Restart", font=("Arial", 12), command=restart, bg='#DEC69C')
restart_button.pack(pady=10) 
canvas.bind("<Button-1>", clicking)




window.mainloop()



