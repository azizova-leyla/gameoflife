#! /usr/bin/env python3

class Board():

    def __init__(self, cells):
        self.cells = cells


class GameOfLife():

    def parse_pattern_file(self, pattern_string):
        coordinates = pattern_string.split(" ")

    def __init__(self, pattern_path):
        with open(pattern_path, "r") as f:
            for line in f:


        self.board = Board(cells)

    def run(self, state):
        pass

if __name__ == "__main__":
    GameOfLife().run()
