import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):

    def test_single_cell_dies(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run("1,1")

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "\n")

    def test_communal_cell_lives(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run("1,1 1,2 2,1 2,2")

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "1,1 1,2 2,1 2,2\n")

    def test_new_cell_lives(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run("1,1 1,2 2,1")

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "1,1 1,2 2,1 2,2\n")
    
    # def test_oscilating_cell(self):
    #     game = GameOfLife()
    #     fake_stdout = io.StringIO()

    #     with contextlib.redirect_stdout(fake_stdout):
    #         game.run("1,1 1,2 2,1 2,2")

    #     output = fake_stdout.getvalue()
    #     fake_stdout.close()

    #     self.assertEqual(output, "1,1 1,2 2,1 2,2")
