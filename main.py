import tkinter as tk
from board import Board as GameBoard
from functools import partial

boards = [[None for _ in range(3)] for _ in range(3)]

PLAYERS = (1, 0)
PLAYER_DISPLAY = {
    0: "O",
    1: "X"
}
current_player = 1
current_board = (-1,-1)


def turn(e_board, e_square):
    global current_player, current_board
    print("clicked square", e_square, "in board", e_board)
    clicked_board = boards[e_board[0]][e_board[1]][1]

    clicked_square = clicked_board[e_square[0]][e_square[1]]
    game = boards[e_board[0]][e_board[1]][2]

    if (current_board == (-1, -1) or e_board == current_board) and game.at(e_square) == -1:
        game.place(current_player, e_square)
        clicked_square.config(text=f'{PLAYER_DISPLAY[current_player]}')

        if boards[e_square[0]][e_square[1]][2].won == False:
            boards[e_square[0]][e_square[1]][0].config(bg='yellow')
            current_board = e_square

        boards[e_board[0]][e_board[1]][0].config(bg='black')
        current_player = PLAYERS[current_player]
        turn_label.config(text=f'{PLAYER_DISPLAY[current_player]} turn')
    else:
        print('illegal')


window = tk.Tk()

window.title("UltimateTicTacToe")
window.minsize(width=1200, height=1000)
window.resizable(False, False)

turn_label = tk.Label(window, text="X turn")
turn_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

pad = tk.Frame(master=window)
pad.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

for i in range(3):
    for j in range(3):
        board = tk.Frame(master=pad,
                         width=300, height=300, relief=tk.RAISED, borderwidth=2, bg="black")
        board.grid(row=i, column=j)
        game = GameBoard()
        squares = [[None for _ in range(3)] for _ in range(3)]

        for s in range(3):
            for t in range(3):
                button = tk.Button(master=board,
                                   width=10, height=5, relief=tk.RAISED, borderwidth=1, bg="pink",
                                   command=partial(turn, (i, j), (s, t)))
                button.grid(row=s, column=t)
                squares[s][t] = button
        boards[i][j] = (board, squares, game)


window.mainloop()
