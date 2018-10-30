# coding: utf-8

import os

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

class NewGrid:

    def __init__(self, datafile):
        self.datafile = datafile
        self.dico = {}

    def setgrid(self):
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + self.datafile, "r") as f:
            line_list = f.read().splitlines()

        # use enumerate to get line_list index. If I use "for line in line_list" I only get the lowest index for the
        # same line in line_list

        for z, line in enumerate(line_list):
            #use enumerate to get charac index. If I use "for charac in line" I only get the lowest index for the
            # same charac in line
            for i,charac in enumerate(line):
                self.dico[(z, i)] = charac
        return self.dico


if __name__ == "__main__":
    grid1 = NewGrid("maze.txt")
    dico_grid1 = grid1.setgrid()
