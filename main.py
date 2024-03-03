import tkinter as tk
from board import Board as GameBoard, WINNING_MOVES
from functools import partial

boards = [[None for _ in range(3)] for _ in range(3)]

PLAYERS = (1, 0)
PLAYER_DISPLAY = {
    0: "O",
    1: "X"
}
COLOR = {
    None: "red",
    0: "pink",
    1: "cyan"
}
current_player = 1
current_board = (-1, -1)


def winner_at(p_board):
    return boards[p_board[0]][p_board[1]][2].won


def check_winner():
    for perm in WINNING_MOVES:
        if winner_at(perm[0]) == winner_at(perm[1]) == winner_at(perm[2]) in [0, 1]:
            print("winner", winner_at(perm[0]), perm)
            return True
    return False


def turn(e_board, e_square):
    global current_player, current_board
    print("clicked square", e_square, "in board", e_board)
    tmp_board = boards[e_board[0]][e_board[1]]
    clicked_board = tmp_board[1]

    clicked_square = clicked_board[e_square[0]][e_square[1]]
    game = tmp_board[2]

    # Is the move valid?
    if ((current_board == (-1, -1) or e_board == current_board) and game.at(e_square) == -1
            and game.won == -1 and not check_winner()):
        game.place(current_player, e_square)
        clicked_square.config(text=f'{PLAYER_DISPLAY[current_player]}')

        # Paint the board accordingly
        board_display = tmp_board[0]
        if game.won != -1:
            board_display.config(bg=COLOR[game.won])
            for squares in clicked_board:
                for square in squares:
                    square.config(bg=COLOR[game.won])
        else:
            board_display.config(bg='black')

        # did anyone win this round?
        if check_winner():
            print("WINNER")
            for bs in boards:
                for b in bs:
                    b[0].config(bg=COLOR[game.won])
            turn_label.config(text=f'{PLAYER_DISPLAY[current_player]} WINS!')
            return

        # Should the next move be on a specific board?
        next_board = boards[e_square[0]][e_square[1]]
        if next_board[2].won == -1:
            next_board[0].config(bg='yellow')
            current_board = e_square
        else:
            current_board = (-1, -1)
        print('current board:', current_board)

        current_player = PLAYERS[current_player]
        turn_label.config(text=f'{PLAYER_DISPLAY[current_player]} turn')
    else:
        print('illegal')


window = tk.Tk()

window.title("UltimateTicTacToe")
window.minsize(width=600, height=500)
window.maxsize(width=1200, height=1000)

turn_label = tk.Label(window, text="X turn")
turn_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

pad = tk.Frame(master=window)
pad.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

for i in range(3):
    for j in range(3):
        board = tk.Frame(master=pad,
                         width=150, height=150, borderwidth=2, bg="black")
        board.grid(row=i, column=j)
        game = GameBoard()
        squares = [[None for _ in range(3)] for _ in range(3)]

        for s in range(3):
            for t in range(3):
                button = tk.Button(master=board,
                                   width=10, height=5, relief=tk.RAISED, borderwidth=1, bg="white",
                                   command=partial(turn, (i, j), (s, t)))
                button.grid(row=s, column=t)
                squares[s][t] = button
        boards[i][j] = (board, squares, game)

window.mainloop()
