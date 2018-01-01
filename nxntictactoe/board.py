
from .svg import draw_board


class Board():

    BLANK = 0

    def __init__(self, rows, cols, n=3):
        self.rows, self.cols, self.n = rows, cols, n
        self.size = rows * cols
        self.reset()

    def reset(self):
        self.turns = 0
        self.data = [Board.BLANK] * self.size
        self.win_cells = []

    def __str__(self):
        out = ""
        for row in range(self.rows):
            for col in range(self.cols):
                out += "{} ".format(self.data[row * self.cols + col])
            out += "\n"
        return out

    def _repr_svg_(self):
        return draw_board(self)

    def set(self, row, col, player_id):
        self.data[row * self.cols + col] = player_id

    def get(self, row, col):
        return self.data[row * self.cols + col]

    def save_win_cells(self, player_id, cells):
        win_cells = []
        for row, col in cells:
            if self.get(row, col) == player_id:
                win_cells += [(row, col)]
            elif len(win_cells) < self.n:
                win_cells = []
            else:
                break
        self.win_cells = win_cells

    def get_win_cells(self):
        return self.win_cells

    def check_range(self, player_id, cells):
        count = 0
        for row, col in cells:
            if self.get(row, col) == player_id:
                count += 1
                if count == self.n:
                    self.save_win_cells(player_id, cells)
                    return True
            else:
                count = 0
        return False

    def check_end(self, row, col, player_id):
        """Check if the given player that makes his last move to (row, col) wins. """
        # Check horizontal.
        h_range = range(max(0, col - self.n), min(self.cols, col + self.n))
        h = self.check_range(player_id, [(row, c) for c in h_range])
        if h: return player_id
        # Check vertical.
        v_range = range(max(0, row - self.n), min(self.rows, row + self.n))
        v = self.check_range(player_id, [(r, col) for r in v_range])
        if v: return player_id
        # Check diagonal that goes up from left to right.
        d1_range = range(v_range[1] + 1, v_range[0] - 1, -1)
        d1 = self.check_range(player_id, [(r, c) for r, c in zip(d1_range, h_range)])
        if d1: return player_id
        # Check diagonal that goes down from left to right.
        d2 = self.check_range(player_id, [(r, c) for r, c in zip(v_range, h_range)])
        if d2: return player_id
        # Check tie.
        self.turns += 1
        if self.turns == self.size:
            return 0
        # No end of game.
        return -1

    def get_legal_movements(self):
        movements = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get(row, col) == Board.BLANK:
                    movements += [(row, col)]
        return movements
