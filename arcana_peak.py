#!/usr/bin/env python
"""Arcana Peak."""
import sys
import os
import time
import cmd
import json
import logging
import blessed
import pygame
# import art

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
logging.basicConfig(filename="debug.log", level=logging.DEBUG)


class Character():
    """Represent a character and all of their statistics."""

    def __init__(self, status, is_npc=False):

        self.status = status
        print("Character spawned. Please kindly welcome " +
              self.status["name"] + " into the world!")

    def __str__(self):
        """String."""
        return str(self.status)

    @property
    def icon(self):
        """Icon."""
        return "[O]"

    def save_to_json(self):
        """Save to JSON."""
        file = open(os.path.join("chars", self.status["name"] + ".json"), "w")
        file.write(json.dumps(self.status))
        file.close()

    def char_from_json(self, file):
        """Import a character from JSON."""
        file = open(file)
        char = json.load(file)
        file.close()
        self.status = char

    def move(self, grid, loc):
        """Move character."""
        grid.move(self, loc)


class Grid():
    """A grid for the game world."""

    def __init__(self, dims):

        self.dims = dims
        self.entities = {}
        self.empty = "[ ]"
        self.squares = [[self.empty for i in range(self.dims[1])]
                        for j in range(self.dims[0])]

    def __str__(self):
        """String."""
        rep = "  "
        for j in range(self.dims[1]):
            rep += " " + str(j) + " "
        for i in range(self.dims[0]):
            rep += "\n" + str(i) + " "
            for j in range(self.dims[1]):
                rep += self.squares[i][j]
        return rep

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
                    sys.stdout.write(text[i+1:])
                    sys.stdout.flush()
                    break
        else:
            time.sleep(speed)
    if is_input:
        return input()
    if new_line:
        print()


def end():
    """End the game."""
    print("Game terminated.")
    print(term.exit_fullscreen)


def display_attributes(user_attributes):
    """Display attributes."""
    for attribute in user_attributes:
        print("You have " + str(user_attributes[attribute]) +
              " " + attribute + ".")
        time.sleep(0.1)


def snarky_quit(message):
    """Quit the game upon too many failed attempts to create a character."""
    clear(confirm=False)
    print_slow(message[:15] + "...\n")
    time.sleep(3)
    print_slow("You know what?")
    time.sleep(1)
    # actually I must have all day since I spent time programming this message
    print_slow("I don't have all day.")
    time.sleep(1)
    print_slow("Maybe this game just isn't for you.")
    time.sleep(5)
    end()


def char_attributes():
    """Allow the player to assign attributes."""
    print_slow("Welcome to attribute assignment.\n")
    time.sleep(1)
    print_slow("Attributes govern how your character "
               "performs at a variety of tasks.")
    print_slow("You have 70 points to distribute among the attributes:")
    for attribute in attributes:
        print(attribute)
        time.sleep(0.5)
    time.sleep(1)
    print_slow("Please choose wisely.\n")
    time.sleep(1)
    user_attributes = {}
    confirm = ""
    attempts = 0
    while confirm.lower() != "yes":
        if attempts == 10:
            snarky_quit("That was a yes or no question, silly! "
                        "I will ask you again.")
        for attribute in attributes:
            while True:
                try:
                    user_attributes[attribute] = int(input(attribute + "\t: "))
                    break
                except ValueError:
                    print("Each attribute must be an integer. "
                          "Please try again.")
        clear()
        display_attributes(user_attributes)
        confirm = input("Before we proceed, please "
                        "confirm if this information is correct. Is it? ")
        if confirm.lower() not in ("yes", "no"):
            print("That was a yes or no question, silly! "
                  "I will ask you again.")
        clear(confirm=False)
    return user_attributes


def char_name():
    """Allow the player to choose a name."""
    confirm = ""
    attempts = 0
    while confirm.lower() != "yes":
        if attempts == 10:
            snarky_quit("I am just asking whether that is your name! "
                        "It isn't that hard of a question. "
                        "A mere yes or no will suffice.")
        name = input("Now I must ask, who are you? ")
        confirm = input("So you are " + name + "? ")
        if confirm.lower() not in ("yes", "no"):
            print("I am just asking whether that is your name! "
                  "It isn't that hard of a question. "
                  "A mere yes or no will suffice.")
            attempts += 1
        clear(confirm=False)
    return name


def char_creation():
    """Allow the player to create a character."""
    play_music("theme.mid")
    user_attributes = char_attributes()
    name = char_name()
    # return the character the player created
    return Character({"name": name,
                      "attributes": user_attributes,
                      "xp": None,
                      "hp": None,
                      "inventory": [],
                      "alignment": None,
                      "class": None,
                      "race": None,
                      "talents": []})


def intro():
    """Intro."""
    play_music("intro.mid")
    intro_text()
    clear()


def intro_text():
    """Intro text."""
    game_credits()
    world_build()


def game_credits():
    """Introduce the game, game's creator, and its licenses."""
    print(term.white_on_black)
    print_slow("Welcome to Arcana Peak: The RPG", speed=0.1)
    print_slow("Arcana Peak: The RPG code is licensed under GNU GPL v3.")
    print_slow("Arcana Peak: The RPG Soundtrack by Dane Campbell "
               "is licensed under CC BY-NC-SA 4.0.")
    clear()
    print(term.normal)


def world_build():
    """World build."""
    print_slow("You are tasked with adventuring "
               "through these lands as you see fit.")
    print_slow("Among the methods available to you are "
               "arcana, might, and diplomacy.")
    print()
    print_slow("To the north, the two Human Kingdoms do little but bicker.")
    print_slow("To the south, the reclusive Ek call the barren desert home.")
    print_slow("In the central mountains, the Arcanists research...")


def play_music(music):
    """Play music."""
    pygame.mixer.music.load("music/" + music)
    pygame.mixer.music.play()


class GameShell(cmd.Cmd):
    """Game shell."""

    def __init__(self, grid):
        super().__init__()
        self.intro = "Type help or ? to list commands."
        self.prompt = str(grid) + "\nState your wish: "
        self.file = None
        self.grid = grid

    def do_move(self, arg):
        """Move a character."""
        clear(confirm=False)
        args = arg.split()
        if args[1] in chars:
            args[1].move(self.grid, args[2].split(", "))
        else:
            print("Sorry, that character does not exist.")

    def do_inventory(self, arg):
        """Check inventory."""
        clear(confirm=False)
        # args = arg.split()
        print("Inventory does not work yet.")

    def do_quit(self, arg):
        """Quit the prompt."""
        return True


def main():
    """Run main."""
    print(term.enter_fullscreen)
    pygame.init()
    intro()
    player = char_creation()
    chars[player.status["name"]] = player
    player.save_to_json()
    grid1 = Grid([10, 10])
    clear()
    GameShell(grid1).cmdloop()
    clear()


if __name__ == "__main__":
    main()
