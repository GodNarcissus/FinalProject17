import random
#allows for speech checks and randomly occuring events
import time
#allows for the text to not all show up at once

class Character(object):
    def __init__(self,name,location):
        self.name = name
        self.location = location
#gives all npc's and the player the same class

map = {"Tutorial"}
#will represent the player's accessable areas

myself = Character("x","Tutorial")
#this is the player!


s = (input("""At what speed would you like the text to show?
1. Fast
2. Normal
(type in the number)
>>> """))

if s == "1":
    s = 1

elif s == "2":
    s = 2

else:
    print("invalid response")
#s is the variable in most time.sleep() instances, whichever number the player chooses will set the game text speed

print('\x1b[5;35;40m' + "Hi! My name is Ashley! Welcome to the dating simulator!" + '\x1b[0m')
#the purple italized text is set for Ashley's dialogue; right now this is an automatic encounter to get the player introduced to someone
time.sleep(s)
#makes sure the text doesn't pop in all at once, giving the player a chance to read everything
print('\x1b[5;35;40m' + "Well, it's more like a friendship simulator because you won't really be dating much." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "But there'll be a lot of people for you to meet and befriend!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "I'm the tutorial lady, and I'll be teaching you the basics of making friends!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + "Now, can you tell me your name?" + '\x1b[0m')
time.sleep(s)
myself.name = input(">>> ")
#the player can choose their name
time.sleep(1)

while True:

    ny = (input('\x1b[5;35;40m' + f"""Is {myself.name} really your name?""" + '\x1b[0m' +
            """
            1. Yes
            2. No

            >>> """))

    if ny == "1":
        print('\x1b[1;37;40m' + "Yes." + '\x1b[0m')
        time.sleep(s)
        break

    elif ny == "2":
        print('\x1b[1;37;40m' + "No." + '\x1b[0m')
        time.sleep(s)
        print('\x1b[5;35;40m' + "It isn't? I must've heard you wrong. What's your name, again?" + '\x1b[0m')
        time.sleep(s)
        myself.name = input(">>> ")

        time.sleep(1)

        ny = (input(f"""{myself.name} is your name, right?
    1. Yes
    2. No

    >>> """))

        if ny == "1":
            print('\x1b[1;37;40m' + "Yes." + '\x1b[0m')
            time.sleep(s)
            break

        elif ny == "2":
            print('\x1b[1;37;40m' + "No." + '\x1b[0m')
            time.sleep(s)
            print('\x1b[5;35;40m' + f"This is too much. I think I'll just call you {myself.name}." + '\x1b[0m')
            time.sleep(s)
            break
        #this feature is just for humor

        elif ny !="1":
            print('\x1b[5;35;40m' + "Excuse me? Sorry, I don't quite get what you mean" + '\x1b[0m')
            time.sleep(1)

    elif ny !="1":
        print('\x1b[5;35;40m' + "Excuse me? Sorry, I don't quite get what you mean" + '\x1b[0m')
        time.sleep(1)

#the loop allows for the player to make sure they get the name they want

print('\x1b[5;35;40m' + f"Hi, {myself.name}! Nice to meet you!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Now, normally people won't approach and talk to you like I just did." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Here, pretend like I didn't already say hi. How would you initiate a conversation?" + '\x1b[0m')
time.sleep(1)
print("use the talkto() function to talk to anyone you'd like. to talk to ashley, do talkto(ashley)")
#a system message because I think it'd be weird for the characters to talk about these functions directly

ashley = Character("Ashley","Tutorial")
#creates Ashley so one can talk to her

#the talkto() function allows for the player to interact with the npc's
def talkto(character):
    if myself.location == character.location:
        print('\x1b[1;37;40m' + f"Hello {character.name}!" + '\x1b[0m')
        time.sleep(s)
        #checks to make sure the player is talking to someone in the same place

        #begins Ashley's speech tree
        if character == ashley:
            print('\x1b[5;35;40m' + f"Hello! Good job, your greeting is quite plain but it does the trick just fine." + '\x1b[0m')
            time.sleep(s)
            r = input('\x1b[5;35;40m' + """Anyways, below is a dialogue branch. Type in the number corresponding the response you'd like to give to my statement.""" + '\x1b[0m' +
            """
            1. Yes
            2. No
            3. Uncertain
            4. Be rude

            >>> """)

            if r == "1":
                print('\x1b[1;37;40m' + "So, like this, right?" + '\x1b[0m')
                time.sleep(s)
                print('\x1b[5;35;40m' + f"Yes! That's perfect, {myself.name}. Easy, right?" + '\x1b[0m')

            elif r == "2":
                print('\x1b[1;37;40m' + "I don't really want to." + '\x1b[0m')
                time.sleep(s)
                print('\x1b[5;35;40m' + "Well even if you didn't, you responded just now." + '\x1b[0m')

            elif r == "3":
                print('\x1b[1;37;40m' + "I'm not too sure how to do this" + '\x1b[0m')
                time.sleep(s)
                print('\x1b[5;35;40m' + "It's alright! You did it just now. Isn't it easy?" + '\x1b[0m')

            elif r == "4":
                print('\x1b[1;37;40m' + "I don't need this stupid tutorial. I know how to talk to people." + '\x1b[0m')
                time.sleep(s)
                print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                time.sleep(1)
                print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                time.sleep(1)
                print('\x1b[5;35;40m' + "Fine! If you think you can make friends without my help go on right ahead!" + '\x1b[0m')
                time.sleep(s)
                r_1 = input("""Ashley storms off and leaves you alone in the Tutorial room. What would you like to do?
                1. Go into the dating simulator without her help.
                2. Try to win back her forgiveness.

                >>> """)

            else:
                print('\x1b[5;35;40m' + "Type in one of the given numbers, I can't understand you." +'\x1b[0m')

            time.sleep(s)

            r = input('\x1b[5;35;40m' + "Below is a speech check. The 3 colors represent the success chance you have of passing it. Try your luck right now." + '\x1b[0m' +
            """
            \x1b[1;32;40m1. 75% success\x1b[0m
            \x1b[1;33;40m2. 50% success\x1b[0m
            \x1b[1;31;40m3. 25% success\x1b[0m
            4. Don't like chance

            >>> """)

            time.sleep(s)

            if r == "1":
                print("nice")

    else:
        print("that person isn't here")
        #in the case the person isn't in the same location or if that person doesn't exist
