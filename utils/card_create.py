import pprint
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_weapon(file_path: str):
    import models.weapon as weapon

    if not os.path.isfile(file_path):
        return "Error: File not found"

    try:
        with open(file_path, 'r') as f:
            name = f.readline().rstrip()
            num_of_desc = int(f.readline())
            description = " ".join([f.readline().rstrip() for _ in range(num_of_desc)])
            new_weapon = weapon.Weapon(name, description)

    except Exception as e:
        return f"Error: {e}"

    return new_weapon


def create_character(file_path: str):
    import models.character as character
    if not os.path.isfile(file_path):
        return "Error: File not found"

    try:
        with open(file_path, 'r') as f:
            name = f.readline().rstrip()
            num_of_desc = int(f.readline())
            description = " ".join([f.readline().rstrip() for _ in range(num_of_desc)])
            new_character = character.Character(name, description)

    except Exception as e:
        return f"Error: {e}"

    return new_character


def create_room(file_path: str):
    import models.room as room
    if not os.path.isfile(file_path):
        return "Error: File not found"

    try:
        with open(file_path, 'r') as f:
            name = f.readline().rstrip()
            num_of_desc = int(f.readline())
            description = " ".join([f.readline().rstrip() for _ in range(num_of_desc)])
            num_of_design = int(f.readline())
            layout = []
            for _ in range(num_of_design):
                layout.append(f.readline().rstrip())
            new_room = room.Room(name, description)
            new_room.set_design(layout)

    except Exception as e:
        return f"Error: {e}"

    return new_room


file_p = os.path.join("..", "asset", "weapons", "test_weapon")
# knife = create_weapon(file_p)
# if isinstance(knife, str):
#     print(knife)
# print(knife.get_name())
# print(knife.get_description())

# file_m = os.path.join("..", "asset", "characters", "test_character")
# mori = create_character(file_m)
# print(mori.get_name())
# print(mori.get_description())

# file_map = os.path.join("..", "asset", "rooms", "test_room")
# main_hall = create_room(file_map)
# print(main_hall.get_name())
# print(main_hall.get_description())
# pprint.pprint(main_hall.get_design())
