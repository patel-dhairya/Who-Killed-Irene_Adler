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


file_p = os.path.join("..", "asset", "weapons", "test_weapon")
knife = create_weapon(file_p)
if isinstance(knife, str):
    print(knife)
print(knife.get_name())
print(knife.get_description())
