
import random

try:
    def _run_from_ipython():
        try:
            __IPYTHON__
            return True
        except NameError:
            return False

    from IPython.display import display

    def _display_board_ipython(board):
        display(board)
except:
    pass

class Game():

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.n_players = len(players)
        assert self.n_players >= 2

    def start(self, first_player=None, display=print):
        self.board.reset()
        if _run_from_ipython():
            display = _display_board_ipython
        if first_player is None:
            first_player = random.randint(0, len(self.players) - 1)
        player = first_player
        win = -1
        print("New game. {}x{} board, connect {}.".format(\
                self.board.rows, self.board.cols, self.board.n))
        display(self.board)
        while True:
            player_id = player + 1
            print("Player", player_id)
            row, col = self.players[player].turn(self.board, player_id)
            self.board.set(row, col, player_id)
            display(self.board)
            win = self.board.check_end(row, col, player_id)
            if win != -1: break
            player = (player + 1) % self.n_players
        if win == 0:
            print("Tie")
        else:
            print("Player {} wins".format(win))
        return win

    def start_fast(self, first_player=0):
        self.board.reset()
        player = first_player
        win = -1
        while win == -1:
            player_id = player + 1
            row, col = self.players[player].turn(self.board, player_id)
            self.board.set(row, col, player_id)
            win = self.board.check_end(row, col, player_id)
            player = (player + 1) % self.n_players
        return win
