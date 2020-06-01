import sys
import time
import os

#Global vars
chars = {}
attributes = ["Strength",
              "Dexterity",
              "Constitution",
              "Intelligence",
              "Wisdom",
              "Will",
              "Favor"]

class Character(object):

    def __init__(self, attributes, talents, status):

        self.name = status["name"]
        print("Character spawned. Please kindly welcome " +
              self.name + " into the world!")
        self.attributes = attributes
        self.status = status
        self.talents = talents

    def __str__(self):

        rep = {"attributes": {}}
        for attribute in attributes:
            rep["attributes"][attribute] = self.attributes[attribute]
        rep["talents"] = self.talents
        rep["status"] = self.status

        return str(rep)

    @property
    def icon(self):

        return "[O]"

    def save_to_json(self):

        f = open(os.path.join("chars", self.name + ".json"), "w")
        f.write(str(self))
        f.close()

class Grid(object):

    def __init__(self, dimensions):

        self.dimensions = dimensions
        self.squares = []
        self.entities = {}
        self.empty = "[ ]"

        for i in range(self.dimensions[0]):

            self.squares.append([self.empty, ]*self.dimensions[1])

    def display(self):

        rep = "  "

        for j in range(self.dimensions[1]):
            rep += " " + str(j) + " "

        for i in range(self.dimensions[0]):
            rep += "\n" + str(i) + " "
            for j in range(self.dimensions[1]):
                rep += self.squares[i][j]

        print(rep)

    def move(self, char, loc):

        if char in self.entities:

            self.squares[self.entities[char][0]][self.entities[char][0]] = self.empty

        self.squares[loc[0]][loc[1]] = char.icon
        self.entities[char] = loc

def clear(confirm=True):

    if confirm:
        input("Press enter to Continue.")

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def char_from_json(file):

    f = open(file)
    char = eval(f.read())
    f.close()
    return Character(char["attributes"], char["talents"], char["status"])

def end():
    print("Game terminated.")
    clear()
    sys.exit()

def inventory():
    print("Inventory does not work yet.")

def move(tokens, active_grid):
    if tokens[1] in chars:
        active_grid.move(chars[tokens[1]], eval(tokens[2]))
    else:
        print("Sorry, that character does not exist.")

def interpret(text, active_grid):

    tokens = text.split(" ")
    commands = {"move": lambda: move(tokens, active_grid), "inventory": lambda: inventory(), "end": lambda: end()}
    if tokens[0] in commands.keys():
        commands[tokens[0]]()
    else:
        print("Your command was not understood. Please check your syntax.")

def char_attributes():

    user_attributes = {}
    clear(confirm=False)
    print("""Welcome to character creation. Here you can assign your attributes.
Your attributes are strength, dexterity, constitution, intelligence, wisdom, will, and finally favor.
You have 70 points to distrobute among them. Please choose wisely.""")
    for attribute in attributes:
        while True:
            try:
                user_attributes[attribute] = int(input("Your character will have this much " + attribute + ": "))
                break
            except:
                print("Each attribute must be an integer. Please try again.")
    clear()
    display_attributes(user_attributes)
    return user_attributes

def display_attributes(attributes):
    for attribute in attributes:
        print("You have " + str(attributes[attribute]) + " " + attribute + ".")

def char_name():
    clear(confirm=False)
    name = input("Now I must ask, who are you? ")
    return name

def char_creation():

    confirm_message = [lambda: "Before we proceed, please confirm if this is correct. Is it? ",
                       lambda: "So you are " + name + "? "]
    fail_message = ["That was a yes or no question, silly! I will ask you again.",
                    "I am just asking whether that is your name! It isn't that hard of a question. A mere yes or no will suffice."]
    user_attributes = {}
    for i in range(2):
        confirm = "no"
        while confirm == "no":
            if i == 0:
                user_attributes = char_attributes()
            else:
                name = char_name()
            confirm = input(confirm_message[i]())
            while confirm.lower() not in ("yes", "no"):
                clear(confirm=False)
                print(fail_message[i])
                if i == 0:
                    display_attributes(user_attributes)
                confirm = input(confirm_message[i]())
    clear(confirm=False)
    return Character(user_attributes, [], {"name":name, "xp":0, "hp":100, "inventory":[], "alignment":None, "class":None, "race":None})

def main():

    print("Welcome to this text-based RPG written in Python.")
    clear()
    player = char_creation()
    chars[player.name] = player
    player.save_to_json()
    clear()
    grid1 = Grid([10, 10])
    grid1.display()

    while True:
        interpret(input("Please enter your command: "), grid1)
        clear()
        grid1.display()
    clear()

main()