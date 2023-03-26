class Character:
    def __init__(self, name: str, description: str):
        """
        Constructor method to initialize a new Character object with a name, description, is_killer property set to
        False, and in_game property set to True.
        :param name (str): Name of character
        :param description (str): Description of character
        """
        self._name = name
        self._description = description
        self._is_killer = False
        self._in_game = True

    # Getter method to retrieve the name of the character
    def get_name(self) -> str:
        return self._name

    # Getter method to retrieve the description of the character
    def get_description(self) -> str:
        return self._description

    # Method to set the character as the killer
    def set_killer(self):
        self._is_killer = True

    # Method to check if the character is the killer
    def is_killer(self) -> bool:
        return self._is_killer

    # Method to set the character as out of the game
    def game_over(self):
        self._in_game = False

    # Method to check if the character is still in the game
    def is_in_game(self) -> bool:
        return self._in_game
