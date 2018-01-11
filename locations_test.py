import time
s = 1
class Character(object):
    def __init__(self):
        self.name = "sir"
        self.location = "A"

myself = Character()

map = {"A", "B", "C"}

"""def travel(destination):
    if destination in map:
        player.location = destination
        print(f"You are now at {destination}")
    else:
        print("That destination isn't on your map.")

def location():
    print(f"You are at {player.location}.")"""

def call_uber():
    print("calling your uber driver...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print('\x1b[0;30;47m' + f"What's up, {myself.name}? Where you wanna go?" + '\x1b[0m')
    time.sleep(1)
    print('\x1b[0;30;47m' + "Just tell me where." + '\x1b[0m')
    time.sleep(1)
    while True:
        #gps()
        print('\x1b[0;30;47m' + "UBER GPS" + '\x1b[0m')
        d = input(">>> ")
        """if d in map:
            print('\x1b[0;30;47m' + "Going there now, my dude." + '\x1b[0m')
            time.sleep(1)
            print("traveling...")
            time.sleep(1)
            myself.location=d
            print('\x1b[0;30;47m' + "Aight we here now. I'll be waiting here if you need me." + '\x1b[0m')
            time.sleep(1)
            print(f"you are now at '{myself.location}.'")
            break"""
        if d == myself.location:
            print('\x1b[0;30;47m' + "My dude we're already here!" + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Don't make me waste my time!" + '\x1b[0m')
        else:
            print('\x1b[0;30;47m' + "I can't find that location in my gps." + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Make sure you tell me the location exactly as it is on your map. Copy & paste it if you need to." + '\x1b[0m')