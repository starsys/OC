# coding: utf-8

from newgrid import *
from pygame_interface import *
from charac import *

""" This is the main program of the game.
grid1 is an instance of Newgrid with maze.txt attribute
setgrid() will create a grid based on maze.txt
then 2 instances of characters will be created
then a Pygame instance is created with attributes: dico_grid1, 2 character's and 3 item's names
The first given character will be considered as "good" and will be movable in the game. 
The second one is fixed and considered as "bad"
items and characters will be showed in the game using the same name ".png" file
"""


grid1 = NewGrid("maze.txt")
dico_grid1 = grid1.setgrid()
macgyver = Charac("macgyver")
gardien = Charac("gardien")
# Pygame instance parameters are : an instance of Newgrid, one instance of "good" character (movable),
# one instance of "bad" character (not movable), any number of item's names to be picked up by the "good" character.
# item's and character's names should be the same as their related png file name. ("macgyver" for "macgyver.png")
pyga1 = Pygame(dico_grid1, macgyver, gardien, "ether", "tube", "aiguille")
pyga1.graphic_maze()
