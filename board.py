PLAYER = {
    "x": 0,
    "o": 1,
    0: "x",
    1: "o"
}

WINNING_MOVES = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2))
]


class Board:
    def __init__(self):
        self.board = [[-1 for _ in range(3)] for _ in range(3)]
        self.won = False

    def at(self, position):
        return self.board[position[0]][position[1]]

    def place(self, player, position):
        # check if board is over or a player is already in that position
        if self.at(position) != -1:
            return False

        self.board[position[0]][position[1]] = PLAYER[player]

        # check for winning player
        for perm in WINNING_MOVES:
            if self.at(perm[0]) == self.at(perm[1]) == self.at(perm[2]):
                self.won = player
                return self.won
