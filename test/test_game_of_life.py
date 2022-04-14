import unittest
import io
import contextlib

from src.game_of_life import GameOfLife
from src.game_of_life import Board

class GameOfLifeTest(unittest.TestCase):

    def test_it_loads_game_state(self):
        pattern_path = "patterns/ship.txt"
        game = GameOfLife(pattern_path=pattern_path)
        board = game.get_board()

        self.assertGreater(board.livingCellsCount(), 0)

    def test_ship_pattern(self):
        pattern_path = "patterns/ship.txt"
        game = GameOfLife(pattern_path=pattern_path)
        board = game.get_board()

        self.assertEqual(board.get_cells()[0:3], [[-2, -44], [-2, -43], [0, -42]])

    def test_it_evolves_one_cell(self):
        board = Board([
            [10, 10]
        ])

        game = GameOfLife(board=board)
        game.run()
        self.assertEqual(game.get_board().get_cells(), [])

#         fake_stdout = io.StringIO()

#         with contextlib.redirect_stdout(fake_stdout):
#         output = fake_stdout.getvalue()
#         fake_stdout.close()

#         self.assertEqual(output, "")


