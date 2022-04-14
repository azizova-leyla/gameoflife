import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):

    def test_load_game_state(self):
        pattern_path = "pattern/ship.txt"
        game = GameOfLife(pattern_path)
#         fake_stdout = io.StringIO()

#         with contextlib.redirect_stdout(fake_stdout):
        board = game.get_board()
        self.assertEqual(board.livingCellsCount(), 10)

#         output = fake_stdout.getvalue()
#         fake_stdout.close()

#         self.assertEqual(output, "")


