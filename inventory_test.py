class Character(object):
    def __init__(self):
        self.location = "A"
        self.inventory = {}

player = Character()

inventory = {"dollars" : 10}

def wallet():
    for key, value in inventory.items():
        print(f"* {key} -- {value}")

def up():
    inventory['dollars'] += 1

def check():
    if "dollars" in inventory:
        print("it works!")

    else:
        print("it doesn't work...")
map = {"store" , "person"}

print(player.inventory)

def store():
    if player.location == "A":
        print("Hello! Welcome to my shop! What would you like to buy?")

        while True:
            purchase = input("""
            1. $5 Buck Lunch -- $5
            2. Bear ----------- $3
            3. Water ---------- $1
            4. Fiji Water ----- $2
            5. leave

            >>>""")

            if purchase == "1":

                if player.inventory["dollars"] >= 5:
                    player.inventory["$5 Buck Lunch"] = 1
                    player.inventory["dollars"] -= 5

                else:
                    print("Sorry! You don't have enough money to buy this!")

            elif purchase == "2":

                if player.inventory["dollars"] >= 3:
                    player.inventory["bear"] = 1
                    player.inventory["dollars"] -= 3

                else:
                    print("Sorry! You don't have enough money to buy this!")

            elif purchase == "3":

                if player.inventory["dollars"] >= 1:
                    player.inventory["water"] = 1
                    player.inventory["dollars"] -= 1

                else:
                    print("Sorry! You don't have enough money to buy this!")

            elif purchase == "4":

                if player.inventory["dollars"] >= 2:
                    player.inventory["fiji water"] = 1
                    player.inventory["dollars"] -= 2

                else:
                    print("Sorry! You don't have enough money to buy this!")

            elif purchase == "5":
                print("Goodbye! Have a nice day!")
                break

            else:
                print("I'm sorry, I didn't quite get that.")

