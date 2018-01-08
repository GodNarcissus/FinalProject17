import random
import time
s = 1

r = input('\x1b[5;35;40m' + "Below is a speech check. The 3 colors represent the success chance you have of passing it. Try to be as charismatic as possible." + '\x1b[0m' +
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

    if k == 1:
        print('\x1b[5;35;40m' + "Yeah you really are a lousy speaker. Oh well, can't be helped." + '\x1b[0m')
        time.sleep(s)

    else:
        print('\x1b[5;35;40m' + "Don't be silly; I think you have a lot of charisma!" + '\x1b[0m')
        time.sleep(s)

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

elif r == "4":
    print('\x1b[1;37;40m' + "I don't know; charisma isn't really my specialty." + '\x1b[0m')
    time.sleep(s)
    print('\x1b[5;35;40m' + "That's fine. Some people are a little more shy than others." + '\x1b[0m')

else:
    print('\x1b[5;35;40m' + "I'm sorry, I don't know what you're trying to say." + '\x1b[0m')
    time.sleep(s)