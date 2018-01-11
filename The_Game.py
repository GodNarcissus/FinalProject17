import random
#allows for speech checks and randomly occuring events
import time
#allows for the text to not all show up at once

class Character(object):
    def __init__(self,name,location):
        self.name = name
        self.location = location
#gives all npc's and the player the same class

map = ["Tutorial"]
#will represent the player's accessable areas

acquaintances = []
#will represent the people the player has already talked to

friends = []
#will represent the people the player has become friends with

myself = Character("x","Tutorial")
#this is the player!

ashley = Character("Ashley","Tutorial")
#this is the tutorial lady

uber = Character("Uber Driver", myself.location)
#this is your uber driver, the person who will transport you to different locations

def gps():
    print("|", end=" ")
    for x in map:
        print(x, end=" | ")
    print('\x1b[1;37;40m' + "MAP" + '\x1b[0m')
        #gives a list of locations on the same line

def contacts():
    print("|", end=" ")
    for x in friends:
        print(x, end=" | ")
    print('\x1b[1;37;40m' + "CONTACTS" + '\x1b[0m')
        #gives a list of friends on the same line

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

def talkto(character):
#the talkto() function allows for the player to interact with the npc's
    if myself.location == character.location:
        print('\x1b[1;37;40m' + f"Hello {character.name}!" + '\x1b[0m')
        time.sleep(s)
        #checks to make sure the player is talking to someone in the same place

        #begins Ashley's speech tree
        if character == ashley:
            if ashley in friends:
                print('\x1b[5;35;40m' + "Hi friend! How are you?" +'\x1b[0m')
            else:
                acquaintances.append(ashley)
                print('\x1b[5;35;40m' + f"Hello! Good job, your greeting is quite plain but it does the trick just fine." + '\x1b[0m')
                time.sleep(s)
                while True:
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
                        break

                    elif r == "2":
                        print('\x1b[1;37;40m' + "I don't really want to." + '\x1b[0m')
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "Well even if you didn't, you responded just now." + '\x1b[0m')
                        break

                    elif r == "3":
                        print('\x1b[1;37;40m' + "I'm not too sure how to do this" + '\x1b[0m')
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "It's alright! You did it just now. Isn't it easy?" + '\x1b[0m')
                        break

                    elif r == "4":
                        print('\x1b[1;37;40m' + "I don't need this stupid tutorial. I know how to talk to people." + '\x1b[0m')
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                        time.sleep(1)
                        print('\x1b[5;35;40m' + "..." + '\x1b[0m')
                        time.sleep(1)
                        print('\x1b[5;35;40m' + "Fine! If you think you can make friends without my help go on right ahead!" + '\x1b[0m')
                        time.sleep(s)
                        while True:
                            r = input("""Ashley storms off and leaves you alone in the Tutorial room. what would you like to do?
                            1. Go into the dating simulator without her help.
                            2. Try to win back her forgiveness.

                            >>> """)
                            if r == "2":
                                print('\x1b[1;37;40m' + "I better go apologize, what I said was wrong." + '\x1b[0m')
                                time.sleep(s)


                            elif r == "1":
                                print('\x1b[1;37;40m' + "Finally, let's start the game already." + '\x1b[0m')
                                time.sleep(s)
                                print("you leave the room and shield your eyes as the sun beams down.")
                                time.sleep(s)
                                print("once your eyes adjust to the light, you see you're now in a park.")
                                time.sleep(s)
                                print("you see some kid playing Tetris on his cellphone.")
                                time.sleep(s)
                                print("you snatch his phone and pull up the map app to see where you are.")
                                time.sleep(s)
                                print("you turn around and realize the tutorial room was just a huge playground.")
                                myself.location = "Joe Collins Park"
                                map.append("Joe Collins Park")
                                print("'Joe Collins Park' has been added to your map!")
                                time.sleep(s)
                                print("type in 'map' without the quotes to see your list of visitable locations.")
                                time.sleep(s)
                                print("by the way, i'm Simi! i'll be with you for the entire game.")
                                time.sleep(s)
                                print("just say hello to me if you have any questions. you did skip the tutorial after all.")
                                time.sleep(s)
                                print("well, you can do as you please now. enjoy the game!")
                                time.sleep(s)
                                break
                            else:
                                print("make a decision.")
                        break

                    else:
                        print('\x1b[5;35;40m' + "Type in one of the given numbers, I can't understand you." +'\x1b[0m')

                    time.sleep(s)

                time.sleep(s)
                while myself.location=="Tutorial":

                    r = input('\x1b[5;35;40m' + "Below is a speech check. The 3 colors represent the success chance you have of passing it. Try your luck right now." + '\x1b[0m' +
                    """
                    \x1b[1;32;40m1. 75% success\x1b[0m
                    \x1b[1;33;40m2. 50% success\x1b[0m
                    \x1b[1;31;40m3. 25% success\x1b[0m
                    4. Don't like chance

                    >>> """)

                    time.sleep(s)

                    if r == "1":
                        print('\x1b[1;37;40m' + "I wouldn't say I'm very charismatic, but I think I can talk just fine." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,4)
                        #creates a random number

                        if k == 1:
                        #25% chance to get a 1; 25% chance to fail check
                            print('\x1b[5;35;40m' + "Yeah you really are a lousy speaker. Oh well, can't be helped." + '\x1b[0m')
                            time.sleep(s)

                        else:
                        #75% not to get a 1; 75% chance to pass check
                            print('\x1b[5;35;40m' + "Don't be silly; I think you have a lot of charisma!" + '\x1b[0m')
                            time.sleep(s)

                        break

                    elif r == "2":
                        print('\x1b[1;37;40m' + "I think I can talk to people just fine." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,2)

                        if k == 1:
                            print('\x1b[5;35;40m' + "Uhh... think again. You might need to work on that." + '\x1b[0m')
                            time.sleep(s)

                        else:
                            print('\x1b[5;35;40m' + "You certainly can! I think you'll be able to make friends pretty easily." + '\x1b[0m')
                            time.sleep(s)

                        break

                    elif r == "3":
                        print('\x1b[1;37;40m' + "I'm an amazing speaker, I can make friends with no problem." + '\x1b[0m')
                        time.sleep(s)
                        k=random.randint(1,4)

                        if k == 1:
                            print('\x1b[5;35;40m' + "Wow, I can see where you're coming from. You're pretty confident too." + '\x1b[0m')
                            time.sleep(s)

                        else:
                            print('\x1b[5;35;40m' + "Um, I don't think so. You might need to tone it down a bit." + '\x1b[0m')
                            time.sleep(s)

                        break

                    elif r == "4":
                        print('\x1b[1;37;40m' + "I don't know; charisma isn't really my specialty." + '\x1b[0m')
                        time.sleep(s)
                        print('\x1b[5;35;40m' + "Some people are a little more shy than others. That's fine." + '\x1b[0m')
                        break

                    else:
                    #prevents user from typing something not fitting
                        print('\x1b[5;35;40m' + "I'm sorry, I don't know what you're trying to say." + '\x1b[0m')
                        time.sleep(s)

                if myself.location == "Tutorial":

                    print('\x1b[5;35;40m' + "You've been doing a great job so far!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "I only have a couple of quick tips to show you before I send you on your way." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Here have this cell phone. It has many uses." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "To look at the locations you can visit in the game, check out the map." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Just say whatever app you want to use, the phone is voice activated." +'\x1b[0m')
                    print("say 'map' without the quotes")
                    while True:
                        a=input(">>> ").lower()
                        if a == "map":
                            gps()
                            break
                        elif a == "hello ashley":
                            print('\x1b[5;35;40m' + "Go ahead, look at the map on the phone I just gave you." +'\x1b[0m')

                    time.sleep(1)
                    print('\x1b[5;35;40m' + "Great! Now, the goal of this game is to make as many friends as possible." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "People will normally give you their number if you're able to befreind them." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can see your friends in your contacts list. Try it now." +'\x1b[0m')
                    time.sleep(1)
                    print("say 'contacts' without the quotes")
                    while True:
                        a=input(">>> ").lower()
                        if a == "contacts":
                            contacts()
                            break
                        elif a == "hello ashley":
                            print('\x1b[5;35;40m' + "Check out your contacts." +'\x1b[0m')

                    time.sleep(1)
                    print('\x1b[5;35;40m' + "Oh right, I just gave you the phone so you won't have any numbers yet." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can have mine then! I'll be your first friend!" +'\x1b[0m')
                    time.sleep(s)
                    print("Ashley is now your friend!")
                    friends.append("Ashley")
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Congratulations! You've finished the tutorial!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "I have one final thing to teach you before you leave." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "To travel to different places in your map, call up an uber." +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "Try looking for more friends at the park nearby, 'Joe Collins.'" +'\x1b[0m')
                    time.sleep(s)
                    map.append("Joe Collins Park")
                    print("'Joe Collins Park' has been added to your map!")
                    time.sleep(s)
                    print('\x1b[5;35;40m' + f"Goodbye, {myself.name}! I hope you'll be able to make more friends soon!" +'\x1b[0m')
                    time.sleep(s)
                    print('\x1b[5;35;40m' + "You can call your uber now to take a look at the park." +'\x1b[0m')
                    time.sleep(s)
                    print("say 'call uber' without the quotes.")
                    while True:
                        a=input(">>> ").lower()
                        if a == "call uber":
                            call_uber()
                            break
                        elif a == "hello ashley":
                            print('\x1b[5;35;40m' + "Call your uber now." +'\x1b[0m')

    else:
        print("that person isn't here")
        #in the case the person isn't in the same location or if that person doesn't exist


while True:
    #s is the variable in most time.sleep() instances, whichever number the player chooses will set the game text speed
    s = (input("""At what speed would you like the text to show?
    1. Fast
    2. Normal
    3. Super Fast (developer speed)
    (type in the number)
    >>> """))

    if s == "1":
        s = 1
        break

    elif s == "2":
        s = 2
        break

    elif s == "3":
        s = 0
        break

    else:
        print("invalid response")
        time.sleep(1)

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

#the loop allows for the player to make sure they get the name they want (at least with a single try)

print('\x1b[5;35;40m' + f"Hi, {myself.name}! Nice to meet you!" + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Now, normally people won't approach and talk to you like I just did." + '\x1b[0m')
time.sleep(s)
print('\x1b[5;35;40m' + f"Here, pretend like I didn't already say hi. How would you initiate a conversation?" + '\x1b[0m')
time.sleep(1)
print("say 'hello ashley' without the quotes to greet Ashley.")
#a system message to be more direct
time.sleep(1)
while True:
    a=input(">>> ").lower()
    if a == "hello ashley":
        talkto(ashley)
        break
time.sleep(1)
print("The park")