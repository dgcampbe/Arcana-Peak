#!/usr/bin/env python
"""Arcana Peak."""
import json
import logging
import os
import sys
import time
import blessed
import cmd2

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

# Global vars
term = blessed.Terminal()
chars = {}
logging.basicConfig(filename="debug.log", level=logging.DEBUG)


class Character:
    """Represent a character and its status."""

    def __init__(self, status, is_npc=False):
        self.status = status
        self.is_npc = is_npc
        print_slow("Character spawned. Please kindly welcome " +
                   self.status["name"] + " into the world!")

    def __str__(self):
        """String."""
        return str(self.status)

    @property
    def icon(self):
        """Icon."""
        return "[O]"

    def save_to_json(self):
        """Save to a JSON file."""
        with open(os.path.join("chars", self.status["name"] + ".json"), "w") as file:
            file.write(json.dumps(self.status))

    def char_from_json(self, file):
        """Import a character from a JSON file."""
        with open(file) as file:
            char = json.load(file)
        self.status = char

    def move(self, grid, loc):
        """Move the character to the desired location on the given grid."""
        grid.move(self, loc)


class Grid:  # Will be replaced with a hex grid.
    """A grid for the game world."""

    def __init__(self, dims):

        self.dims = dims
        self.entities = {}
        self.empty = "[ ]"
        self.squares = [[self.empty] * self.dims[1] for i in range(self.dims[0])]

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

    def move(self, char, loc, place=True):
        """
        Move a character on the grid.

        Parameters
        ----------
        char : Character
            Character that will be moved.
        loc : Tuple
            Location to which the character will be moved.
        place : bool, optional
            Determines if the character is placed if it isn't already placed.

        Returns
        -------
        None.

        """
        if char in self.entities:
            current_loc = self.entities[char]
            self.squares[current_loc[0]][current_loc[1]] = self.empty
        if char in self.entities or place:
            self.squares[loc[0]][loc[1]] = char.icon
            self.entities[char] = loc


def clear(confirm=True):
    """Clear the console window after an optional user confirmation."""
    if confirm:
        input("\nPress enter to continue.")
    print(term.clear)


def print_slow(text="", speed=0.025, new_line=True,
               is_input=False, skip=True):
    """
    Slowly print text across the screen, mimicking manually typed text.

    Parameters
    ----------
    text: str
        The text that will be printed.
    speed: float, optional
        The amount of time, in seconds, spent asleep between characters
        with extra time spent on certain punctuation and at the end.
        The default is 0.025
    new_line: bool, optional
        Determines if the printing should begin on a new line.
        The default is True.
    is_input: bool, optional
        Determines if the slow print behaves like the input function,
        except with the prompt being given in a slowly printed fashion.
        The default is False.
    skip: bool, optional
        Determines if the player is able to skip the rest of slow
        printing by pressing space.
        The default is True.

    """
    for i, char in enumerate(text):
        if char in [" ", ",", ".", ":", ";", "!", "?"]:
            time.sleep(speed * 3)
        sys.stdout.write(char)
        sys.stdout.flush()
        if skip:
            with term.cbreak():
                val = term.inkey(timeout=speed)
                if val == " ":
                    sys.stdout.write(text[i + 1:])
                    sys.stdout.flush()
                    break
        else:
            time.sleep(speed)
    time.sleep(speed * 10)
    if is_input:
        return input()
    if new_line:
        print()


def end():
    """End the game."""
    print("Game terminated.")
    print(term.exit_fullscreen)
    sys.exit()


def snarky_quit(message):
    """Quit the game upon too many failed attempts to create a character."""
    clear(confirm=False)
    print_slow(message[:15] + "...\n")
    time.sleep(3)
    print_slow("You know what?")
    time.sleep(1)
    # actually I have all day, I had the time to program this message
    print_slow("I don't have all day.")
    time.sleep(1)
    print_slow("Maybe this game just isn't for you.")
    time.sleep(5)
    end()


def char_name():
    """Allow the player to choose a name."""
    clear(confirm=False)
    failure_text = """I am just asking whether that is your name!
    It really isn't that hard of a question.
    A mere yes or no will suffice."""
    confirm = "no"
    attempts = 0
    allowed_failures = 5
    name = None
    while confirm.lower() != "yes":
        if attempts == allowed_failures:
            snarky_quit(failure_text)
            break
        name = print_slow("Now I must ask, who are you? ", is_input=True)
        confirm = print_slow("So you are " + name + "? ", is_input=True)
        if confirm.lower() not in ("yes", "no"):
            print_slow(failure_text)
            attempts += 1
        clear(confirm=False)
    return name


def char_creation():
    """
    Allow the player to create a character.

    Returns
    -------
    Character
        The character that the player created.

    """
    play_music("theme.mid")
    print_slow("Welcome to character creation.")
    clear()
    name = char_name()
    # return the character the player created
    return Character({"name": name,
                      "attributes": None,
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
    """Introduce the game, game's creator, and licenses."""
    print_slow("Welcome to Arcana Peak: The RPG")
    print_slow("Arcana Peak: The RPG code is licensed under "
               f"{term.link('https://www.gnu.org/licenses/gpl-3.0.en.html', 'GNU GPL v3')}.")
    print_slow("Arcana Peak: The RPG Soundtrack by Dane Campbell "
               "is licensed under "
               f"{term.link('https://creativecommons.org/licenses/by-nc-sa/4.0/', 'CC BY-NC-SA 4.0')}.")
    clear()


def world_build():
    """World build."""
    print_slow("You are tasked with adventuring "
               "through these lands as you see fit.")
    print_slow("Among the methods available to you are "
               "arcana, might, and diplomacy.")
    print_slow()
    print_slow("To the north, the two Human Kingdoms do little but bicker.")
    print_slow("To the south, the reclusive Ek call the barren desert home.")
    print_slow("In the central mountains, the Arcanists research...")


def play_music(music):
    """
    Play a music file.

    Parameters
    ---------
    music: str
        The name of the music file to be played.

    """
    pygame.mixer.music.load("music/" + music)
    pygame.mixer.music.play()


parser = cmd2.Cmd2ArgumentParser()
parser.add_argument("char", help="Character that will be moved.")
parser.add_argument("loc", help="Location to move to.")
parser2 = cmd2.Cmd2ArgumentParser()
parser2.add_argument("char", help="Character whose inventory to check.")


class GameShell(cmd2.Cmd):
    """Game shell."""

    def __init__(self, grid):
        super().__init__()
        self.intro = "Type help or ? to list commands."
        self.file = None
        self.grid = grid
        self._set_prompt()
        self.register_postcmd_hook(self.postcmd_hook_method)

    def postcmd_hook_method(self, data: cmd2.plugin.PostcommandData) -> cmd2.plugin.PostcommandData:
        """

        Parameters
        ----------
        data

        Returns
        -------

        """
        clear()
        self._set_prompt()
        return data

    def _set_prompt(self):
        """Set prompt."""
        self.prompt = str(self.grid) + "\nState your wish: "

    @cmd2.decorators.with_argparser(parser)
    def do_move(self, opts):
        """Move a character to a location on the grid."""
        if opts.char in chars:
            chars[opts.char].move(self.grid, tuple(map(int, opts.loc.split(","))))
        else:
            print("Sorry, that character does not exist.")

    @cmd2.decorators.with_argparser(parser2)
    def do_inventory(self, opts):
        """Check inventory."""
        if opts.char in chars:
            print("Inventory does not work yet.")
        else:
            print("Sorry, that character does not exist.")


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
    end()


if __name__ == "__main__":
    main()
