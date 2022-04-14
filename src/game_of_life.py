#! /usr/bin/env python3

class Board():

    def __init__(self, cells):
        self.cells = cells

    def livingCellsCount(self):
        return len(self.cells)

    def get_cells(self):
        return self.cells

class GameOfLife():

    def parse_pattern_file(self, pattern_string):
        coordinates = pattern_string.split(" ")
        cells = [[int(x) for x in string.split(",")] for string in coordinates]

        return cells

    def __init__(self, pattern_path=None, board=None):
        if not pattern_path is None:
            with open(pattern_path, "r") as f:
                self.board = Board(self.parse_pattern_file(f.read()))

        if not board is None:
            self.board = board

    def get_board(self):
        return self.board

    def run(self):
        self.board = Board([])

if __name__ == "__main__":
    GameOfLife().run()
