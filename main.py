# -*- coding: utf8 -*-

from newgrid import *
from pygame_interface import *
from charac import *

""" Create "dico dictionnary" based on a given "maze.txt" containing some lines of characters. 
This .txt file represent the maze we want to create. Each character of each line symbolize a maze block.
Block_types :
"S" = maze start
"A" = maze arrival
"W" = maze wall
"P" = maze path
dico.keys are tuples. Each index correspond to line index (2 digits) and row index (2 digits) coordinates.
dico.values are block_types ("S", "A", "W" or "P")
example : if maze's arrival is at the 2nd block of the 7th line, you'll find following value in dico : {(07, 01) = "A"}
"""


if __name__ == "__main__":

    grid1 = NewGrid("maze.txt")
    dico_grid1 = grid1.setgrid()
    macgyver = Charac("macgyver")
    gardien = Charac("gardien")
    # Pygame instance parameters are : an instance of Newgrid, one instance of "good" character (movable),
    # one instance of "bad" character (not movable), any number of item's names to be picked up by the "good" character.
    # item's and character's names should be the same as their related png file name. ("macgyver" for "macgyver.png")
    pyga1 = Pygame(dico_grid1, macgyver, gardien, "ether", "tube", "aiguille")
    pyga1.graphic_maze()
