#! /usr/bin/env python3

class Board():

    def __init__(self, cells):
        self.cells = cells

    def livingCellsCount(self):
        return len(self.cells)

class GameOfLife():

    def parse_pattern_file(self, pattern_string):
        coordinates = pattern_string.split(" ")
        return [map(int, string.split(",")) for string in coordinates]


    def __init__(self, pattern_path):
        with open(pattern_path, "r") as f:
            self.board = Board(self.parse_pattern_file(f.read()))

    def get_board(self):
        return self.board

    def run(self, state):
        pass

if __name__ == "__main__":
    GameOfLife().run()
