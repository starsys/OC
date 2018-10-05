# -*- coding: utf8 -*-

import os

""" Create "dico dictionnary" based on given "datafile.txt" containing some lines of characters. 
This .txt file represent the maze we want to create. Each character of each line symbolize a maze block.
Block_types :
"S" = maze start
"A" = maze arrival
"W" = maze wall
"P" = maze path
dico.keys are each block lines (2 digits) and rows (2 digits) coordinates.
dico.values are block_types
example : if maze's arrival is the 2nd block of 7th line, you'll find following value in dico : {0701 = "A"}
"""

class NewGrid:

    def __init__(self, datafile):
        self.datafile = datafile

    def setgrid(self):
        dico = {}
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + self.datafile, "r") as f:
            line_list = f.read().splitlines()
            print(line_list)
        for line in line_list:
            #use enumerate to get charac index. If I use "for charac in line" I only get the lowest index for the
            # same charac in line
            for i,charac in enumerate(line):
                dico["{:02d}".format(line_list.index(line)) + "{:02d}".format(i)] = charac
        print(dico)



class Character:

    def __init__(self, good):
        self.good = good


if __name__ == "__main__":
    grid1 = NewGrid("maze.txt")
    grid1.setgrid()
