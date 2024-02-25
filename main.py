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


def turn(board, square):
    global current_player
    print("clicked square", square, "in board", board)
    c_board = boards[board[0]][board[1]][1]

    c_square = c_board[square[0]][square[1]]
    c_game = boards[board[0]][board[1]][2]
    if c_game.at(square) == -1:
        c_game.place(current_player, square)
        c_square.config(text=f'{PLAYER_DISPLAY[current_player]}')

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
                         width=300, height=300, relief=tk.RAISED, borderwidth=2, bg="yellow")
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
