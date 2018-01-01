
import random


from .board import Board


class Agent():

    def __init__(self):
        pass

    def turn(self, board, player_id):
        legal_movements = board.get_legal_movements()
        return random.choice(legal_movements)


class Player():

    def _read_input(self):
        try:
            row_col = input("Row, Column: ")
            row, col = eval(row_col)
            return row, col
        except:
            return 0, 0

    def turn(self, board, player_id):
        row, col = self._read_input()
        while row > board.rows or col > board.cols or row < 1 or col < 1\
                or board.get(row - 1, col - 1) != Board.BLANK:
            print("Error: 1 <= row <= {} and 1 <= col <= {} and cell must be blank"\
                    .format(board.rows, board.cols))
            row, col = self._read_input()
        return row - 1, col - 1
