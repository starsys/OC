# -*- coding: utf8 -*-

import os

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
