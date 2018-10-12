# -*- coding: utf8 -*-

import pygame
import os

class Pygame:

    def __init__(self, maze_dico):
        self.maze_dico = maze_dico
        pass

    def get_max_line(self):
        nb_lines = []
        return max([key[0] for key in self.maze_dico.keys()])

    def get_max_row(self):
        nb_rows = []
        return max([key[1] for key in self.maze_dico.keys()])


    def graphic_maze(self):

        BLOCK_PX_SIZE = 30

        x_resolution = (self.get_max_line() + 1) * BLOCK_PX_SIZE
        y_resolution = (self.get_max_row() + 1) * BLOCK_PX_SIZE

        pygame.init()

        # Pygame window opening
        fenetre = pygame.display.set_mode((y_resolution, x_resolution))

        # backgroung load and display
        fond = pygame.image.load(os.path.dirname(__file__) + "/" + "images" + "/" + "background.jpg").convert()

        fenetre.blit(fond, (0, 0))

        # maze graphic content load and display based on txt file
        wall = pygame.image.load(os.path.dirname(__file__) + "/" + "images" + "/" + "wall.png").convert_alpha()

        for key, value in self.maze_dico.items():
            # wall picture size is 30 px * 30 px
            if value == "W":
                fenetre.blit(wall, (key[1] * 30, key[0] * 30))

        # Screen refresh
        pygame.display.flip()

        # infinite loop
        continuer = 1

        while continuer:
            continuer = int(input())

if __name__ == "__main__":
    pyga1 = Pygame(dico_grid1)
    pyga1.graphic_maze()