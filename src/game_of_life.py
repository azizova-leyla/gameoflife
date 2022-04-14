#! /usr/bin/env python3

class GameOfLife():
    def run(self, state):
        if len(state) > 6:
            print(state)
        else:
            print('')

if __name__ == "__main__":
    GameOfLife().run()
