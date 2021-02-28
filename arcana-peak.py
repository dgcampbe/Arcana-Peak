#!/usr/bin/env python
"""rpg."""
import sys
import os
import multiprocessing as mp
import time
import blessed
# import logging

# Global vars
term = blessed.Terminal()
chars = {}
attributes = ["Strength",
              "Dexterity",
              "Constitution",
              "Intelligence",
              "Wisdom",
              "Will",
              "Favor"]


class Character():
    """Represent a character and all of their statistics."""

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


class Grid():
    """A grid for the game world."""

    def __init__(self, dims):

        self.dims = dims
        self.entities = {}
        self.empty = "[ ]"
        self.squares = [[self.empty for i in range(self.dims[1])]
                        for j in range(self.dims[0])]

    def display(self):
        """Display."""
        rep = "  "
        for j in range(self.dims[1]):
            rep += " " + str(j) + " "
        for i in range(self.dims[0]):
            rep += "\n" + str(i) + " "
            for j in range(self.dims[1]):
                rep += self.squares[i][j]
        print(rep)

    def move(self, char, loc):
        """Move."""
        if char in self.entities:
            entity = self.entities[char]
            self.squares[entity[0]][entity[1]] = self.empty
        self.squares[loc[0]][loc[1]] = char.icon
        self.entities[char] = loc


def clear(confirm=True):
    """Clear the console window after an optional user confirmation."""
    if confirm:
        input("\nPress enter to Continue.")
    print(term.clear)


def print_slow(text, speed=0.05, new_line=True,
               is_input=False, skippable=True):
    """Slowly print text across the screen."""
    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        if skippable:
            with term.cbreak():
                val = term.inkey(timeout=speed)
                if val == " ":
                    break
        else:
            time.sleep(speed)
    sys.stdout.write(text[i+1:])
    sys.stdout.flush()
    if is_input:
        return input()
    if new_line:
        print()


def char_from_json(file):
    """Import a character from JSON."""
    f = open(file)
    char = eval(f.read())
    f.close()
    return Character(char["status"])


def end():
    """End the game."""
    print("Game terminated.")
    print(term.exit_fullscreen)


def list_commands():
    """Commands."""
    print("Available commands are:")
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
                "end": lambda: end(), "help": lambda: list_commands()}
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
    time.sleep(5)
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
        time.sleep(0.1)


def char_name():
    """Character name."""
    clear(confirm=False)
    name = input("Now I must ask, who are you? ")
    return name


def snarky_quit(message):
    """Quit the game upon too many failed attempts to create a character."""
    clear(confirm=False)
    print_slow(message[:15] + "...\n")
    time.sleep(3)
    print_slow("You know what?")
    time.sleep(1)
    # actually I must have all day
    # since I spent time programming this message to work
    print_slow("I don't have all day.")
    time.sleep(1)
    print_slow("Maybe this game just isn't for you.")
    time.sleep(5)
    end()


def char_creation():
    """Character creation."""
    proc = mp.Process(target=play_music, args=("theme.mid",))
    proc.start()
    print_slow("Welcome to character creation.\n")
    time.sleep(1)
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
    proc.join()
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
    proc = mp.Process(target=play_music, args=("intro.mid",))
    proc.start()
    intro_text()
    proc.join()
    clear()


def intro_text():
    """Intro text."""
    game_credits()
    world_build()


def game_credits():
    """Introduce the game's creator and its licenses."""
    print(term.white_on_black)
    print_slow("Welcome to Arcana Peak: The rpg", speed=0.1)
    print_slow("Arcana Peak: The rpg code is licensed under GNU GPL v3.")
    print_slow("Arcana Peak: The rpg Soundtrack by Dane Campbell "
               "is licensed under CC BY-NC-SA 4.0.")
    print(term.normal)
    clear()


def world_build():
    """World Build."""
    print_slow("You are tasked with adventuring "
               "through these lands as you see fit.")
    print_slow("Among the methods available to you are "
               "arcana, might, and diplomacy.")
    print()
    print_slow("To the north,  the two Human Kingdoms do little but bicker.")
    print_slow("To the south,  the reclusive Ek call the barren desert home.")
    print_slow("In the central mountains, the Arcanists research...")


def play_music(music):
    """Play music."""
    if os.name == "nt":
        os.system("fluidsynth -ni C:/soundfonts/default.sf2 music/"
                  + music + " > debug.log")
    else:
        os.system("fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 music/"
                  + music + " > debug.log")


def main():
    """Main."""
    print(term.enter_fullscreen)
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


if __name__ == "__main__":
    main()
