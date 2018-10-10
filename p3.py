# -*- coding: utf8 -*-

import os
import pygame

""" Create "dico dictionnary" based on given "datafile.txt" containing some lines of characters. 
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

class NewGrid:

    def __init__(self, datafile):
        self.datafile = datafile

    def setgrid(self):
        dico = {}
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + self.datafile, "r") as f:
            line_list = f.read().splitlines()

        for line in line_list:
            #use enumerate to get charac index. If I use "for charac in line" I only get the lowest index for the
            # same charac in line
            for i,charac in enumerate(line):
                dico["{:02d}".format(line_list.index(line)) + "{:02d}".format(i)] = charac
        # print(dico)
        return dico

class Pygame:

    def __init__(self, maze_dico):
        self.maze_dico = maze_dico
        pass

    def graphic_maze(self):
        pygame.init()

        # Pygame window opening

        fenetre = pygame.display.set_mode((450, 450))

        # backgroung load and display


        fond = pygame.image.load(os.path.dirname(__file__) + "/" + "background.jpg").convert()

        fenetre.blit(fond, (0, 0))

        # maze graphic content load and display based on txt file

        wall = pygame.image.load(os.path.dirname(__file__) + "/" + "wall.png").convert_alpha()
        for key, value in self.maze_dico.items():
            # wall picture size is 30 px * 30 px
            if value == "W":
                fenetre.blit(wall, (int(key[2:4]) * 30, int(key[0:2]) * 30))


        # Screen refresh

        pygame.display.flip()

        # infinite loop

        continuer = 1

        while continuer:
            continuer = int(input())


class Character:

    def __init__(self, good):
        self.good = good
        self.position = "0000"
        self.inventory = {}



if __name__ == "__main__":
    grid1 = NewGrid("maze.txt")
    dico = grid1.setgrid()
    pyga1 = Pygame(dico)
    pyga1.graphic_maze()


