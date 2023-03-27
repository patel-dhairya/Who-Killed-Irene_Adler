# Game class that will draw the board
import pprint


class Game:
    def __init__(self):
        self._game_start = True
        self._board = []
        self.add_board()

    def add_board(self):
        width = 150
        height = 32

        self._board.append("_" * width)
        for i in range(height - 2):
            self._board.append("|" + " " * (width - 2) + "|")

        self._board.append("|" + "_" * (width - 2) + "|")

    def draw_board(self):
        for row in self._board:
            print(row)

    def replace_character(self, y, x, character):
        location = list(self._board[y])
        location[x] = character
        new_string = "".join(location)
        self._board[y] = new_string


# New = Game()
# New.replace_character(16, 75, "S")
# New.replace_character(20, 75, "M")
# New.draw_board()
