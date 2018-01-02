class Character(object):
    def __init__(self):
        self.location = "A"

player = Character()

map = {"A", "B", "C"}

def travel(destination):
    if destination in map:
        player.location = destination
        print(f"You are now at {destination}")
    else:
        print("That destination isn't on your map.")

def location():
    print(f"You are at {player.location}.")
