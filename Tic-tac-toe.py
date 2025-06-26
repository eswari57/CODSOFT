import tkinter as tk
from tkinter import messagebox
import random

board = [" " for _ in range(9)]

# Minimax Algorithm for unbeatable AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Chooses the move that is best for AI
def best_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Used to check for the winner. If the O's and X's are same in the below specified coordinates then it prints the winning message
def check_winner(b):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

# Allows user to enter the input by simply clicking the grids
def click(i):
    if board[i] == " " and not check_winner(board):
        board[i] = "X"
        buttons[i]["text"] = "X"
        buttons[i]["fg"] = "#ff007f"  # Rose pink for player
        if check_winner(board):
            end_game("You win! 🎉")
            return
        elif " " not in board:
            end_game("It's a draw! 🤝")
            return
        root.after(300, ai_turn)

# It's AI. it uses the best_move() to fills with O
def ai_turn():
    move = best_move()
    if move is not None:
        board[move] = "O"
        buttons[move]["text"] = "O"
        buttons[move]["fg"] = "#3a7bd5"  # Soft blue for AI
        if check_winner(board):
            end_game("AI wins! 💻")

# A message pops up to display the winner
def end_game(message):
    messagebox.showinfo("Game Over", message)
    for btn in buttons:
        btn.config(state="disabled")

# It clears the board and resets the game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal", fg="black")

# For GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe ✨ | You vs AI")
root.configure(bg="#f0e6f6")  # Soft pastel purple

title = tk.Label(root, text="Tic-Tac-Toe 🎮", font=("Comic Sans MS", 24, "bold"), bg="#f0e6f6", fg="#6a0dad")
title.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    btn = tk.Button(root, text=" ", width=8, height=4,
                    font=("Arial", 20, "bold"),
                    bg="#ffe4f0",  # Light pink
                    activebackground="#ffc0cb",  # Brighter pink on click
                    command=lambda i=i: click(i))
    btn.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12, "bold"),
                      bg="#dcd6f7", fg="black", command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
