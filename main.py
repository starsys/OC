# coding: utf-8

from newgrid import *
from pygame_interface import *
from charac import *

""" This is the main program of the game.
- setgrid() will create a grid based on maze.txt
- 2 instances of characters are created
- .graphic_maze() method is applied on a Pygame instance with attributes: dico_grid1, 2 character's and 3 item's names
The first given character will be considered as "good" and will be movable in the game. 
The second one is fixed and considered as "bad"
items and characters will be showed in the game using the same name ".png" file
"""


dico_grid1 = NewGrid("maze.txt").setgrid()
macgyver = Charac("macgyver")
gardien = Charac("gardien")
# Pygame instance parameters are : an instance of Newgrid, one instance of "good" character (movable),
# one instance of "bad" character (not movable), any number of item's names to be picked up by the "good" character.
# item's and character's names should be the same as their related png file name. ("macgyver" for "macgyver.png")
Pygame(dico_grid1, macgyver, gardien, "ether", "tube", "aiguille").graphic_maze()
