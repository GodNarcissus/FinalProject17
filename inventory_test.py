class Character(object):
    def __init__(self):
        self.location = "A"
        self.inventory = {}

player = Character()

player.inventory = {"dollars" : 10}

map = {"store" , "person"}

def talkto(object):
    if object not in map:
        print(f"you can't talk to {object} here.")
    elif
