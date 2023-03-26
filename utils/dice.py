import random


class Dice:
    def __init__(self, sides=6):
        """
        Constructor for Dice class. Initializes the number of sides on the dice.

        Args:
        - sides (int): Number of sides on the dice (default 6).
        """
        self._sides = sides

    def roll(self):
        """
        Simulates rolling the dice and returns a random number between 1 and the number of sides.

        Returns:
        - int: Random number between 1 and the number of sides on the dice.
        """
        return random.randint(1, self._sides)
