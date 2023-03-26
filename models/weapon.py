class Weapon:
    def __init__(self, name: str, description: str):
        """
        Constructor method to initialize a new weapon object with a name, description and is_murder_weapon property set
        to False.
        :param name (str): Name of weapon
        :param description (str): Description of weapon
        """
        self._name = name
        self._description = description
        self._is_murder_weapon = False

    # Getter method to retrieve the name of the weapon
    def get_name(self) -> str:
        return self._name

    # Getter method to retrieve the description of the weapon
    def get_description(self) -> str:
        return self._description

    # Method to set the weapon as the murder weapon
    def set_murder_weapon(self):
        self._is_murder_weapon = True

    # Method to check if the weapon is the murder weapon
    def is_murder_weapon(self) -> bool:
        return self._is_murder_weapon
