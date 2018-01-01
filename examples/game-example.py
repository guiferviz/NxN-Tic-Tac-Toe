
import nxntictactoe as ttt


# Create board.
rows = 3
columns = 3
connect = 3
b = ttt.Board(rows, columns, connect)
# Random player.
p1 = ttt.Agent()
# Player that ask the user the next movement.
p2 = ttt.Player()
# Create a game with that board and those 2 players.
g = ttt.Game(b, [p1, p2])
# Run the game in verbose mode.
winner = g.start()

print("Winner", winner)
