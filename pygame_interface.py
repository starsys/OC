# -*- coding: utf8 -*-

import pygame
import os

class Pygame:

    def __init__(self, maze_dico):

        self.maze_dico = maze_dico
        pass

    def graphic_maze(self):

        BLOCK_PX_SIZE = 30

        lines_list = []
        rows_list = []

        for coordinates in self.maze_dico.keys():
            lines_list.append((coordinates)[0:2])
            rows_list.append((coordinates)[2:4])

        x_resolution = (int(max(rows_list)) + 1) * BLOCK_PX_SIZE
        y_resolution = (int(max(lines_list)) + 1) * BLOCK_PX_SIZE

        pygame.init()

        # Pygame window opening

        fenetre = pygame.display.set_mode((x_resolution, y_resolution))

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

