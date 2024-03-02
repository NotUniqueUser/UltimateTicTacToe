PLAYER = {
    "x": 1,
    "o": 0,
    1: "x",
    0: "o"
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
        self.won = -1

    def at(self, position):
        return self.board[position[0]][position[1]]

    def place(self, player, position):
        # check if board is over or a player is already in that position
        if self.at(position) != -1:
            return False

        self.board[position[0]][position[1]] = PLAYER[player]

        # check for winning player
        print('checking if',PLAYER[player],'won')
        for perm in WINNING_MOVES:
            if self.at(perm[0]) == self.at(perm[1]) == self.at(perm[2]) != -1:
                self.won = player
                print("player", PLAYER[player], "won")
                return self.won
        # check for stalemate
        flag = False
        for row in self.board:
            if -1 in row:
                flag = True
        if not flag:
            self.won = None
            print('stalemate')
