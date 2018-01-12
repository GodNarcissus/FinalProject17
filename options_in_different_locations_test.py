import time
s=0

class Character(object):
    def __init__(self,name,location):
        self.name = name
        self.location = location

myself = Character("me" , "A")
#uber = Character("Uber Driver" , myself.location)

map = ["A", "B", "C"]
visited = ["A"]

def gps():
    print("|", end=" ")
    for x in map:
        print(x, end=" | ")
    print('\x1b[1;37;40m' + "MAP" + '\x1b[0m')
        #gives a list of locations on the same line

def uber():
    print("calling your uber driver...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print('\x1b[0;30;47m' + f"What's up, {myself.name}? Where you wanna go?" + '\x1b[0m')
    time.sleep(1)
    print('\x1b[0;30;47m' + "Just tell me where." + '\x1b[0m')
    time.sleep(1)
    while True:
        gps()
        d = input(">>> ")
        if d == myself.location:
            print('\x1b[0;30;47m' + "My dude we're already here!" + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Don't make me waste my time!" + '\x1b[0m')
        elif d in map:
            print('\x1b[0;30;47m' + "Going there now, my dude." + '\x1b[0m')
            time.sleep(1)
            print("traveling...")
            time.sleep(1)
            myself.location=d
            uber.location=d
            print('\x1b[0;30;47m' + "Aight we here now. I'll be waiting here if you need me." + '\x1b[0m')
            time.sleep(1)
            print(f"you are now at '{myself.location}.'")
            break
        else:
            print('\x1b[0;30;47m' + "I can't find that location in my gps." + '\x1b[0m')
            time.sleep(s)
            print('\x1b[0;30;47m' + "Make sure you tell me the location exactly as it is on your map. Copy & paste it if you need to." + '\x1b[0m')


while True:
    if myself.location == "A":
        a = input(">>> ")
        if a == "call uber":
            uber()
    elif myself.location == "B":
        if "B" not in visited:
            visited.append("B")
            print("this is 'B'")
        else:
            print("you've been here before")

        a = input(">>> ")
        if a == "call uber":
            uber()
    elif myself.location == "C":
        a = input(">>> ")
        if a == "call uber":
            uber()

