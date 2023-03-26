class Room:
    def __init__(self, name: str, description: str):
        """
        Constructor method to initialize a new room object with a name, description and is_crime_scene, secret_passage
        property set to False.
        :param name (str): Name of room
        :param description (str): Description of room
        """
        self._name = name
        self._description = description
        self._is_crime_scene = False
        self._secret_passage = []

    # Getter method to retrieve the name of the room
    def get_name(self) -> str:
        return self._name

    # Getter method to retrieve the description of the room
    def get_description(self) -> str:
        return self._description

    # Method to check if the room is a crime scene
    def is_crime_scene(self) -> bool:
        return self._is_crime_scene

    # Method to set the room as the crime scene
    def set_crime_scene(self):
        self._is_crime_scene = True

    def set_secret_passage(self, new_room: 'Room'):
        self._secret_passage.append(new_room)

    def is_passage_available(self) -> bool:
        return len(self._secret_passage) != 0
