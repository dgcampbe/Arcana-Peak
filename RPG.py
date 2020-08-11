#!/usr/bin/env python
"""rpg."""
import sys
import os
import keyboard
import threading
import time
# import fabulous
# import logging

# Global vars
chars = {}
attributes = ["Strength",
              "Dexterity",
              "Constitution",
              "Intelligence",
              "Wisdom",
              "Will",
              "Favor"]


class Character(object):
    """Represent a character and all of their statisics."""

    def __init__(self, status, is_npc=False):

        self.status = status
        print("Character spawned. Please kindly welcome " +
              self.status["name"] + " into the world!")

    def __str__(self):
        """String."""
        rep = ""
        for i in self.status:
            rep += i + ": " + str(self.status[i])
        return str(rep)

    @property
    def icon(self):
        """Icon."""
        return "[O]"

    def save_to_json(self):
        """Save to JSON."""
        f = open(os.path.join("chars", self.status["name"] + ".json"), "w")
        f.write(str(self))
        f.close()


class Grid(object):
    """A grid for the game world."""

    def __init__(self, dimensions):

        self.dimensions = dimensions
        self.squares = []
        self.entities = {}
        self.empty = "[ ]"

        for i in range(self.dimensions[0]):

            self.squares.append([self.empty, ]*self.dimensions[1])

    def display(self):
        """Display."""
        rep = "  "

        for j in range(self.dimensions[1]):
            rep += " " + str(j) + " "

        for i in range(self.dimensions[0]):
            rep += "\n" + str(i) + " "
            for j in range(self.dimensions[1]):
                rep += self.squares[i][j]

        print(rep)

    def move(self, char, loc):
        """Move."""
        if char in self.entities:
            self.squares[self.entities[char][0]][self.entities[char][0]] = self.empty
        self.squares[loc[0]][loc[1]] = char.icon
        self.entities[char] = loc


def clear(confirm=True):
    """Clear the console window after an optional user confirmation."""
    if confirm:
        input("\nPress enter to Continue.")
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def print_slow(text, speed=0.05, new_line=True,
               is_input=False, skippable=True):
    """Slowly print text across the screen."""
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        if skippable:
            rest(speed)
        else:
            time.sleep(speed)
    sys.stdout.write(text[i+1:])
    if is_input:
        return input()
    if new_line:
        print()


def char_from_json(file):
    """Import a character from JSON."""
    f = open(file)
    char = eval(f.read())
    f.close()
    return Character(char["attributes"], char["talents"], char["status"])


def end():
    """End the game."""
    print("Game terminated.")
    clear()
    sys.exit()


def commands():
    """Commands."""
    print("Avalible commands are:")
    print("move <character> (row,column) "
          "- move <character> to the spot at (row, column)")
    print("inventory - checks your inventory")
    print("end - ends the game")
    print("help - displays this help page")


def inventory():
    """Check inventory."""
    print("Inventory does not work yet.")


def move(tokens, active_grid):
    """Move."""
    if tokens[1] in chars:
        active_grid.move(chars[tokens[1]], eval(tokens[2]))
    else:
        print("Sorry, that character does not exist.")


def interpret(text, active_grid):
    """Interpret the commands input by the user."""
    tokens = text.split(" ")
    commands = {"move": lambda: move(tokens, active_grid),
                "inventory": lambda: inventory(),
                "end": lambda: end(), "help": lambda: commands()}
    if tokens[0] in commands.keys():
        commands[tokens[0]]()
    else:
        print("Your command was not understood. Please check your syntax.")


def char_attributes():
    """Character attributes."""
    user_attributes = {}
    print("It is time to assign your attributes.")
    print("Your attributes are strength, dexterity, constitution, "
          "intelligence, wisdom, will, and finally favor.")
    print("These will govern how your character "
          "performs at a variety of tasks.")
    print("You have 70 points to distribute among them.\n")
    rest(5)
    print_slow("Please choose wisely.\n")
    for attribute in attributes:
        while True:
            try:
                user_attributes[attribute] = int(input(
                    "Your character will have this much " + attribute + ": "))
                break
            except ValueError:
                print("Each attribute must be an integer. Please try again.")
    clear()
    display_attributes(user_attributes)
    return user_attributes


def display_attributes(attributes):
    """Display attributes."""
    for attribute in attributes:
        print("You have " + str(attributes[attribute]) + " " + attribute + ".")
        rest(0.1)


def char_name():
    """Character name."""
    clear(confirm=False)
    name = input("Now I must ask, who are you? ")
    return name


def snarky_quit(message):
    """Quit the game unpon too many failed attempts to create a character."""
    clear(confirm=False)
    print_slow(message[:15] + "...\n")
    rest(3)
    print_slow("You know what?")
    rest(1)
    # actually I must have all day
    # since I spent time programming this message to work
    print_slow("I don't have all day.")
    rest(1)
    print_slow("Maybe this game just isn't for you.")
    rest(5)
    end()


def char_creation():
    """Character creation."""
    event = threading.Event()
    thread = threading.Thread(target=play_music,
                              args=(event, "theme.mid"), daemon=True)
    thread.start()
    print_slow("Welcome to character creation.\n")
    rest(1)
    clear()
    confirm_message = [lambda: "Before we proceed, "
                       "please confirm if this is correct. Is it? ",
                       lambda: "So you are " + name + "? "]
    fail_message = ["That was a yes or no question, silly! "
                    "I will ask you again.",
                    "I am just asking whether that is your name! "
                    "It isn't that hard of a question. "
                    "A mere yes or no will suffice."]
    user_attributes = {}
    for i in range(2):
        confirm = "no"
        j = 0
        while confirm.lower() != "yes":
            clear(confirm=False)
            if j == 10:
                snarky_quit(fail_message[i])
            if i == 0:
                user_attributes = char_attributes()
            elif i == 1:
                name = char_name()
            confirm = input(confirm_message[i]())
            while confirm.lower() not in ("yes", "no"):
                clear(confirm=False)
                j += 1
                if j == 10:
                    snarky_quit(fail_message[i])
                # provide a snarky message
                # informing the user about their failure
                print_slow(fail_message[i])
                if i == 0:
                    display_attributes(user_attributes)
                confirm = print_slow(confirm_message[i](), is_input=True)
            j += 1
    event.wait()
    clear()
    # return the character the player created
    return Character({"name":  name,
                      "attributes": user_attributes,
                      "xp": None,
                      "hp": None,
                      "inventory": [],
                      "alignment": None,
                      "class": None,
                      "race": None,
                      "talents": []})


def intro():
    """Introduce the game, its creator, and licenses."""
    event = threading.Event()
    event2 = threading.Event()
    thread = threading.Thread(target=intro_text,
                              args=(event,), daemon=True)
    thread2 = threading.Thread(target=play_music,
                               args=(event2, "intro.mid"), daemon=True)
    thread.start()
    thread2.start()
    event2.wait()
    clear()


def intro_text(event):
    """Intro text."""
    game_credits()
    world_build()
    event.set()


def game_credits():
    """Introduce the game's creator and its licenses."""
    print_slow("Welcome to this text-based "
               "RPG written in Python.\n", speed=0.1)
    print_slow("rpg code is licensed under GNU GPL v3.")
    print_slow("rpg Soundtrack by Dane Campbell "
               "is licensed under CC BY-NC-SA 4.0.")
    clear()


def world_build():
    """World Build."""
    print_slow("You are tasked with adventuring "
               "through these lands as you see fit.")
    print_slow("Amoung these methods are arcana, might, and diplomacy.")


def detect_skip(event):
    """Detect skip."""
    while not event.isSet():
        if keyboard.is_pressed("space"):
            event.set()
            break


def rest(length):
    """Rest."""
    event = threading.Event()
    thread = threading.Thread(target=detect_skip, args=(event,), daemon=True)
    thread.start()
    event.wait(length)


def play_music(event, music):
    """Play music."""
    os.system("timidity music/" + music + " > debug.log")
    event.set()


def main():
    """Main."""
    clear(confirm=False)
    intro()
    player = char_creation()
    chars[player.status["name"]] = player
    player.save_to_json()
    grid1 = Grid([10, 10])
    clear()
    grid1.display()
    while True:
        interpret(input("Please enter your command: "), grid1)
        clear()
        grid1.display()
    clear()


main()
