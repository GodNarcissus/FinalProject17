import random
#allows for speech checks and randomly occuring events
import time
#allows for the text to not all show up at once

class Character(object):
    def __init__(self,name,location,speech):
        self.name = name
        self.location = location
        self.speech = speech

map = {"Tutorial"}

myself = Character("x","Tutorial","""Why are you talking to yourself? Make some friends!""")
#this is the player!

s = int(input("""At what speed would you like the text to show?
1. Fast
2. Normal
(type in the number)
>>> """))

print('\x1b[5;35;40m' + "Hi! My name is Ashley! Welcome to the dating simulator!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "Well, it's more like a friendship simulator because you won't really be dating much." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "But there'll be a lot of people for you to meet and befriend!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "I'm the tutorial lady, and I'll be teaching you the basics of making friends!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "Now, can you tell me your name?" + '\x1b[0m')
time.sleep(s)
myself.name = input(">>> ")
time.sleep(1)
print('\x1b[5;35;40m' + f"Hi, {myself.name}! Nice to meet you!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Now, normally people won't approach and talk to you like I just did." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Here, pretend like I didn't already say hi. How would you initiate a conversation?" + '\x1b[0m')
time.sleep(1)
print("use the talkto() function to talk to anyone you'd like. to talk to ashley, do talkto(ashley)")

ashley = Character("Ashley","Tutorial",'\x1b[5;35;40m' + """Hello! Seems like your social skills need some work but they're good enough for now!""" + '\x1b[0m')

def talkto(character):
    if myself.location == character.location:
        print(f"Hello {character.name}!")
        print(character.speech)

    else:
        print("that person isn't here")

"""def print_format_table():

    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()"""
