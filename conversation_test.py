import time
import random
#allows for the text to show after a pause and for there to be success/failure chances

n = input("\033[1;35mhi ! i'm nora ! what's your name ? >> \033[1;m")
#has the person ask for user's name and her chat text is pink

while True:
    r = input("""1. be friendly
2. be rude
3. ask to go out
""")
#gives the user 3 text options with different outcomes

    if r == "1":
        print(f"Hi, my name is {n}. Nice to meet you.")

        time.sleep(1)

        while True:
            r_1 = input(f"""\033[1;35mhi {n} ! what are you doing here at this ice cream social ?\033[1;m
        \033[1;33m1. try to be cool\033[1;m
        2. give a genuine answer
        3. ask for her number""")

            if r_1 == "1":
                print("Talking to this girl with the prettiest eyes I've ever seen.")
                time.sleep(1)
                s = random.randint(1,2)

                if s == 1:
                    print("\033[1;35mmarry me already oml\033[1;m")
                    #lives happily ever after
                    break

                else:
                    print("\033[1;35mew ! go away !\033[1;m")
                    #gets rejected
                    break

            elif r_1 == "2":
                print("I'm here to get some ice cream.")
                time.sleep(1)
                print("\033[1;35moh cool\033[1;m")
                time.sleep(1)
                print('\033[1;30mThe girl turns back around and waits for her ice cream in line.\033[1;m')
                break

            elif r_1 == "3":
                print("Hey! Can I get your number?")
                time.sleep(1)
                print("\033[1;35mumm sure\033[1;m")
                time.sleep(1)
                print('\033[1;30mThe girl reluctantly gives you her number. The look on her face tells you she will not call you back.\033[1;m')
                break

            else:
                print("\033[1;35mi don't quite understand what you mean . what did you say ?\033[1;m")
                #lets the user have another chance to type 1, 2, or 3

        break

    elif r == "2":
        print("Kill yourself.")
        time.sleep(1)
        print("\033[1;35mmarry me already oml\033[1;m")
                    #lives happily ever after

        break

    elif r == "3":
        print(f"I'm {n}. Do you wanna go out?")
        time.sleep(1)
        print('\033[1;30mThe girl laughs at you and walks away. It seems like you got rejected.\033[1;m')
        break

    else:
        print("\033[1;35mi don't quite understand what you mean . what did you say ?\033[1;m")
        #lets the user have another chance to type 1, 2, or 3