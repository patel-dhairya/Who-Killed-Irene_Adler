class Room:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._is_crime_scene = False

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
