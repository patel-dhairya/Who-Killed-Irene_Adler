class Player:
    """
    A class representing a player in a game.
    """
    def __init__(self, name: str):
        """
        Initialize a new player with a name, an empty list of cards, and
        the player is still in game (True).
        """
        self._name = name
        self._cards = []
        self._in_game = True
        self._location = [0, 0]

    def get_name(self) -> str:
        """
        Return the name of the player.
        """
        return self._name

    def add_card(self, card) -> None:
        """
        Add a card to the player's list of cards. If a list of cards is provided,
        all cards in the list will be added to the player's list of cards.
        """
        if isinstance(card, list):
            self._cards.extend(card)
        elif isinstance(card, str):
            self._cards.append(card)

    def get_cards(self) -> list:
        """
        Return a list of the player's cards.
        """
        return self._cards

    def game_over(self) -> None:
        """
        Set the player's game status to False to indicate that the game is over
        for this player.
        """
        self._in_game = False

    def get_location(self) -> list:
        """
        Return the current location of the player as a list of coordinates [x, y].
        """
        return self._location

    def set_location(self, new_xy) -> str:
        """
        Update the player's location to the given coordinates [x, y].
        If the input format is incorrect, return an error message.
        Otherwise, return a confirmation message.
        """
        if not len(new_xy) == 2:
            return "Error : Location of player should be in [x, y] format"
        if not (isinstance(new_xy[0], int) and isinstance(new_xy[1], int)):
            return "Error : Location of player should be in [x, y] format where x and y are integer"
        self._location = new_xy
        return f"Player moved to {self._location[0], self._location[1]}."
