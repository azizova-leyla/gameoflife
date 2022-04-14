#! /usr/bin/env python3

class GameOfLife():
    def run(self, state):
        if len(state) > 6:
            pairs = state.split(" ")
            if len(pairs) == 3:
                print(state + " 2,2")
            else:
                print(state)
        else:
            print('')

if __name__ == "__main__":
    GameOfLife().run()
