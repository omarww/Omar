

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.configure(background="black")

# Create the game board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Create the buttons for the game board
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text="", font=('Arial', 60), width=4, height=2, command=lambda i=i, j=j: play(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Create the turn indicator
turn_indicator = Label(root, text="Player 1's turn", font=('Arial', 20))
turn_indicator.grid(row=3, columnspan=3)

# Define the play function
def play(row, col):
    global board
    if board[row][col] == '':
        if turn_indicator['text'] == "Player 1's turn":
            buttons[row][col]['text'] = "X"
            board[row][col] = "X"
            turn_indicator['text'] = "Player 2's turn"
        else:
            buttons[row][col]['text'] = "O"
            board[row][col] = "O"
            turn_indicator['text'] = "Player 1's turn"
        check_win()

# Define the check_win function
def check_win():
    global board
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winner = board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '':
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
    if winner:
        messagebox.showinfo("Winner", f"{winner} wins!")
        root.destroy()
    elif all([all(row) for row in board]):
        messagebox.showinfo("Tie", "It's a tie!")
        root.destroy()

root.mainloop()


