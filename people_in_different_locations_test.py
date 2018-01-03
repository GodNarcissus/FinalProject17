class Character(object):
    def __init__(self, location):
        self.location = location
        self.inventory = {}

player = Character("A")

npc = Character("A")

def talkto(character):
    if player.location == character.location:
        print("Hello!")

    else:
        print("that person isn't here")