# -*- coding: utf8 -*-

from newgrid import *
from pygame_interface import *

""" Create "dico dictionnary" based on a given "maze.txt" containing some lines of characters. 
This .txt file represent the maze we want to create. Each character of each line symbolize a maze block.
Block_types :
"S" = maze start
"A" = maze arrival
"W" = maze wall
"P" = maze path
dico.keys are each block lines (2 digits) and rows (2 digits) coordinates.
dico.values are block_types ("S", "A", "W" or "P")
example : if maze's arrival is at the 2nd block of th e7th line, you'll find following value in dico : {0701 = "A"}
"""


if __name__ == "__main__":

    grid1 = NewGrid("maze.txt")
    dico_grid1 = grid1.setgrid()
    pyga1 = Pygame(dico_grid1)
    pyga1.graphic_maze()
